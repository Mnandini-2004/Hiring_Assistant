# memory.py

import streamlit as st

# Initialize session memory and state
def init_session():
    """
    Initialize session state variables for chatbot interaction.
    """
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "conversation_stage" not in st.session_state:
        st.session_state.conversation_stage = "greeting"
    if "candidate_info" not in st.session_state:
        st.session_state.candidate_info = {
            "Full Name": None,
            "Email Address": None,
            "Phone Number": None,
            "Years of Experience": None,
            "Desired Position": None,
            "Current Location": None,
            "Tech Stack": None,
        }

def update_stage(stage):
    """
    Update the current stage of the conversation.

    Parameters:
        stage (str): New conversation stage.
    """
    st.session_state.conversation_stage = stage

def save_candidate_info(key, value):
    """
    Save candidate information in session state.

    Parameters:
        key (str): Field name to update.
        value (any): Value to set for the field.
    """
    st.session_state.candidate_info[key] = value

def get_stage():
    """
    Retrieve the current stage of the conversation.

    Returns:
        str: Current conversation stage.
    """
    return st.session_state.conversation_stage

def get_candidate_info():
    """
    Retrieve the candidate's information.

    Returns:
        dict: Candidate information dictionary.
    """
    return st.session_state.candidate_info

def add_message(role, content):
    """
    Add a message to the chat history.

    Parameters:
        role (str): Sender role ("user" or "assistant").
        content (str): Message content.
    """
    st.session_state.messages.append({"role": role, "content": content})

def get_chat_history():
    """
    Retrieve the chat history.

    Returns:
        list: List of chat messages.
    """
    return st.session_state.messages

def clear_session():
    """
    Clear all session state data.
    """
    st.session_state.clear()

