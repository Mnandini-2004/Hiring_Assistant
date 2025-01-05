import os
from groq import Groq

'''
# Function to query Groq's Llama model
def query_groq(prompt):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",  # Specify the correct model ID
        stream=False,
    )
    return chat_completion.choices[0].message.content'''

# Here we create client for Groq API, using key that is given. Groq lets us use Llama model for chat.
# helpers.py

import os
from groq import Groq
#from transformers import pipeline

# Initialize Groq client
client = Groq(api_key="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")


def query_groq(prompt, history=[]):
    """
    Query Groq's LLM model with a given prompt and conversation history.
    
    Parameters:
        prompt (str): The user's input for the model.
        history (list): List of previous messages in the conversation.

    Returns:
        str: Model's response to the input prompt.
    """
    messages = [{"role": "system", "content": "You are a hiring assistant chatbot for technical screening."}]
    messages += history
    messages.append({"role": "user", "content": prompt})
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",  # Specify the correct model ID
        stream=False,
    )
    return chat_completion.choices[0].message.content


# Load sentiment analysis pipeline
#sentiment_analyzer = pipeline("sentiment-analysis")

'''def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text using a sentiment analysis model.
    
    Parameters:
        text (str): Input text to analyze.
    
    Returns:
        dict: Sentiment result containing label and score.
    """
    result = sentiment_analyzer(text)[0]
    return result'''

