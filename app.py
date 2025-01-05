


import streamlit as st
from utils.helpers import query_groq#, analyze_sentiment
from utils.memory import init_session, add_message, get_chat_history, update_stage, save_candidate_info, get_stage, get_candidate_info
from utils.memory import clear_session
import re

import streamlit as st



# Load prompt templates
def load_prompt(filename):
    with open(f"prompts/{filename}", "r") as file:
        return file.read()

# Initialize session state
init_session()

# Sidebar Information
st.sidebar.title("TalentScout")
st.sidebar.info(
    """
    Welcome to TalentScout, a leading tech recruitment agency. 
    This chatbot will guide you through an initial screening process.
    """
)

# Chatbot Title
st.title("TalentScout Hiring Assistant Chatbot")

# Display Chat History
for msg in get_chat_history():
    st.chat_message(msg["role"]).write(msg["content"])

# Validation functions
def validate_name(name):
    if not name.isalpha() or len(name.split()) < 2:
        return False, "Please enter a valid full name (only alphabets and spaces allowed)."
    return True, ""

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return False, "Please enter a valid email address."
    return True, ""

def validate_phone(phone):
    if not phone.isdigit() or len(phone) != 10:
        return False, "Please enter a valid 10-digit phone number."
    return True, ""

def validate_experience(experience):
    if not experience.isdigit() or int(experience) < 0 or int(experience) > 40:
        return False, "Please enter a valid number of years of experience (0-40)."
    return True, ""

def validate_tech_stack(tech_stack):
    if not tech_stack.strip():
        return False, "Tech stack cannot be empty."
    return True, ""

# Start Conversation with Greeting
if get_stage() == "greeting":

    
    greeting = load_prompt("greeting_prompt.txt")
    initial_response = query_groq(greeting)
    add_message("assistant", initial_response)
    st.chat_message("assistant").write(initial_response)
    update_stage("ask_name")

# User Input

user_input = st.chat_input("Type your response here...", key="unique_chat_input")


if user_input:
    
    

    st.chat_message("user").write(user_input)
    add_message("user", user_input)
    response = query_groq(user_input, get_chat_history())


    # Stage-based logic
    current_stage = get_stage()
        
    if current_stage == "ask_name":
        is_valid, message = validate_name(user_input)
        if is_valid:
            response = message
        else:
            save_candidate_info("Full Name", user_input)
            update_stage("ask_email")
            response = "Thank you! Could you please share your Email Address?"
        
    elif current_stage == "ask_email":
        is_valid, message = validate_email(user_input)
        if not is_valid:
            response = message
        else:
            save_candidate_info("Email Address", user_input)
            update_stage("ask_phone")
            response = "Got it! What's your Phone Number?"
        
    elif current_stage == "ask_phone":
        is_valid, message = validate_phone(user_input)
        if not is_valid:
            response = message
        else:
            save_candidate_info("Phone Number", user_input)
            update_stage("ask_experience")
            response = "Great! How many years of experience do you have?"
        
    elif current_stage == "ask_experience":
        is_valid, message = validate_experience(user_input)
        if not is_valid:
            response = message
        else:
            save_candidate_info("Years of Experience", user_input)
            update_stage("ask_position")
            response = "Nice! What position are you applying for?"
        
    elif current_stage == "ask_position":
        save_candidate_info("Desired Position", user_input)
        update_stage("ask_location")
        response = "Understood! Could you tell me your current location?"
        
    elif current_stage == "ask_location":
        save_candidate_info("Current Location", user_input)
        update_stage("ask_tech_stack")
        response = "Thank you! Lastly, what technologies, programming languages, and tools are you proficient in (Tech Stack)?"
        
    elif current_stage == "ask_tech_stack":
        is_valid, message = validate_tech_stack(user_input)
        if not is_valid:
            response = message
        else:
            save_candidate_info("Tech Stack", user_input)
            candidate_info = get_candidate_info()
            
            # Generate Technical Questions
            tech_stack = candidate_info["Tech Stack"]
            desired_position = candidate_info["Desired Position"]
                
            # Split the tech stack to handle diverse technologies
            tech_list = [tech.strip() for tech in tech_stack.split(",")]
            formatted_tech_stack = ", ".join(tech_list)

            tech_prompt = load_prompt("tech_stack_prompt.txt").format(
            tech_stack=formatted_tech_stack, position=desired_position
            )
            response = query_groq(tech_prompt)
            
            update_stage("technical_questions")



        
    elif current_stage == "technical_questions":
        response = query_groq(user_input, get_chat_history())
        '''sentiment = analyze_sentiment(user_input)
        if sentiment["label"] == "NEGATIVE" and sentiment["score"] > 0.7:
            response = "I noticed you might be feeling a bit negative. Is there anything I can help with?"
            add_message("assistant", response)
            st.chat_message("assistant").write(response)'''
          

    

        
    else:
        response = load_prompt("fallback_prompt.txt")
        
    add_message("assistant", response)
    st.chat_message("assistant").write(response)


   
if st.sidebar.button("End Conversation"):
    clear_session()
    st.sidebar.success("Session cleared. Thank you for your time!")
    st.rerun()

# Clear Data Button
if st.sidebar.button("Clear Data"):
    st.session_state.candidate_info = {}
    st.session_state.messages = []
    st.success("All candidate data cleared.")


# Sidebar for options
with st.sidebar:
    st.header("Options")
    send_feedback = st.button("Send Feedback")
    
# Show feedback form when the button is pressed
if send_feedback:
    st.title("Feedback Form")
    with st.form("feedback_form"):
        feedback = st.text_area("Let us know your feedback!")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you for your feedback!")
