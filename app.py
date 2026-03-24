import streamlit as st
from langserve import RemoteRunnable

# Streamlit framework implementation
st.title("Langchain Demo With Llama2 API (Frontend)")

input_text = st.text_input("Search the topic you want to know about")

# Connect to the FastAPI backend
# Ensure the server in main.py is running on http://localhost:8000
chain = RemoteRunnable("http://localhost:8000/chatbot")

def get_response(input_text):
    try:
        response = chain.invoke({"question": input_text})
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"

if input_text:
    st.write(get_response(input_text))