from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables from .env
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', '')
os.environ['LANGCHAIN_TRACING_V2'] = "true"  # Should be 'LANGCHAIN_TRACING_V2' for newest LangChain
os.environ['LANGCHAIN_ENDPOINT'] = "https://api.smith.langchain.com"
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY', '')
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT', 'ChatBot')

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A Simple API Server"
)

# Standard Output Parser
output_parser = StrOutputParser()

# 1. Simple OpenAI Route
add_routes(
    app,
    ChatOpenAI() | output_parser,
    path="/openai"
)

# 2. OpenAI Essay Chain
model = ChatOpenAI()
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")

add_routes(
    app,
    prompt1 | model | output_parser,
    path="/essay"
)

# 3. Ollama (Llama2) Poem Chain
llm = Ollama(model="llama2")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5-year-old child with 100 words")

add_routes(
    app,
    prompt2 | llm | output_parser,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)