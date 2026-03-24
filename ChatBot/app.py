import streamlit as st
from langserve import RemoteRunnable
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langsereve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama

load_dotenv()



# Streamlit framework implementation
st.title("Langchain Demo With Llama2 API (Frontend)")

input_text = st.text_input("Search the topic you want to know about")

# Connect to the FastAPI backend
# Ensure the server in main.py is running on http://localhost:8000
chain = RemoteRunnable("http://localhost:8000/chatbot")

def get_response(input_text):
    try:
        response = chain.invoke({"question": input_text})
        # Handle cases where response is a string (like from Ollama) 
        # or a Message object (like from OpenAI Chat)
        if hasattr(response, 'content'):
            return response.content
        return str(response)
    except Exception as e:
        return f"Error: {str(e)}"

if input_text:
    st.write(get_response(input_text))