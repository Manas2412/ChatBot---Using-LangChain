import streamlit as st
import requests

def get_openai_response(topic):
    # Using the standardized backend response (direct string)
    response = requests.post("http://localhost:8000/essay/invoke", json={"input": {"topic": topic}})
    return response.json()["output"]

def get_ollama_response(topic):
    # Using the standardized backend response (direct string)
    response = requests.post("http://localhost:8000/poem/invoke", json={"input": {"topic": topic}})
    return response.json()["output"]

# Streamlit framework
st.title("LangChain Client (Multi-LLM)")

input_essay = st.text_input("Write an essay on topic:")
input_poem = st.text_input("Write a poem on topic:")

if input_essay:
    st.write(get_openai_response(input_essay))

if input_poem:
    st.write(get_ollama_response(input_poem))
