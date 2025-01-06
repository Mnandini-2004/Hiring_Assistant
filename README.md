# Hiring Assistant Chatbot

## Project Overview
The Hiring Assistant Chatbot is an intelligent conversational tool designed to assist a fictional recruitment agency, TalentScout, in automating the initial screening process of potential candidates. This chatbot:

1.📋 Gathers essential candidate details (e.g., name, email, experience, and tech stack).
2.✅ Validates the inputs for accuracy and completeness.
3.🛠️ Asks technical questions based on the candidate’s provided tech stack and preffered position.
4.🤖 Provides a natural conversational experience using advanced Large Language Models (LLMs).
5.🧠 Incorporates sentiment analysis to gauge candidate responses and adapt the interaction accordingly.
6.🔒 Ensures focus by avoiding irrelevant questions and keeping the conversation strictly recruitment-oriented.
7.📚 Recommends learning resources to candidates with insufficient knowledge, encouraging skill development.
8.🗑️ Provides an option to clear all data, ensuring candidate privacy and compliance with data protection standards.

This project demonstrates the seamless integration of conversational AI with recruitment workflows, improving efficiency and user experience.

## Installation Instructions
Follow the steps below to set up and run the chatbot locally:

### Prerequisites
Ensure the following are installed:
🐍 Python 3.8 or higher
📦 pip (Python package manager)

### Steps
1. Clone the Repository
   ```bash
   git clone https://github.com/Mnandini-2004/Hiring_Assistant
   cd Hiring_Assistant
   ```

2. Set Up a Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Application
   ```bash
   streamlit run app.py
   ```

5. Access the Chatbot
   Open your browser and navigate to:
   ```
   http://localhost:8501
   ```


## Usage Guide

1. Start the Chatbot
   🚀 Launch the app and interact with the chatbot from the main page.

2. Follow the Chatbot Prompts
   - 📄 Provide your details such as full name, email address, phone number, years of experience, current location, and desired tech stack.
   - 🛠️ Answer the technical questions generated based on your expertise.

3. Session Management
   - ⚙️ Use the sidebar options to clear data or end the conversation.
   - 💬 Provide feedback through the feedback form.


## Technical Details

### Libraries Used
🖥️ Streamlit: Front-end framework for interactive UI.
📚 Transformers: Provides pre-trained models for sentiment analysis.
🤖 Groq API: Leveraged for LLM capabilities (Llama model).
🔍 Regex: Input validation for email, phone numbers, and other fields.

### Models
🧠 **LLM (Llama-3.3-70b-versatile)**: Handles conversation and technical question generation.
😊 **Sentiment Analysis Transformer Model**: Detects positive, negative, or neutral tones in candidate responses.

### Architecture
The project follows a modular structure:
1. 🛠️ `helpers.py`: Manages LLM queries and sentiment analysis.
2. 💾 `memory.py`: Handles session state for conversation flow and data persistence.
3. 🚀 `app.py`: Main script integrating logic, UI, and interaction.


## Prompt Design
Crafting prompts was a critical part of this project to ensure the chatbot’s efficiency and accuracy:

✨ Greeting Prompt: Sets a warm, professional tone to engage candidates.
📜 Tech Stack Prompt: Dynamically generates technical questions based on the provided stack.
🔄 Fallback Prompt: Ensures seamless recovery from unrecognized inputs.

Example of a tech stack prompt:
```
Based on the candidate’s expertise in {formatted_tech_stack}, and their interest in a {desired_position}, generate 3-8 technical questions that assess their skills.
```


## Challenges & Solutions

### Challenge 1: Input Validation
- Problem: Ensuring accurate and valid inputs from users.
- Solution: Implemented regex-based validation for fields like email and phone number with detailed error messages.

### Challenge 2: Dynamic Question Generation
- Problem: Generating context-aware and relevant technical questions.
- Solution: Designed adaptive prompts using user-provided tech stack and desired position.

### Challenge 3: Sentiment Analysis Integration
- Problem: Gauging user sentiment during interactions.
- Solution: Integrated a sentiment analysis pipeline to adapt the chatbot’s responses and offer support when necessary.

### Challenge 4: Data Security Integration
- Problem: Candidate data security at stake
- Solution: Provided options to clear data after completion.


This Hiring Assistant Chatbot not only streamlines the recruitment process but also demonstrates the potential of AI in creating impactful real-world solutions.

