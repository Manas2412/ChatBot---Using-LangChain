from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# LLM model
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please provide response to the user queries"),
    ("user", "Question:{question}")
])

# Add routes to the FastAPI app
add_routes(
    app,
    prompt | llm | StrOutputParser(),
    path="/chatbot",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
