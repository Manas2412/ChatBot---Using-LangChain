# LangChain ChatBot with FastAPI & Streamlit

This project demonstrates how to build a ChatBot using LangChain, served via a FastAPI/LangServe backend and a Streamlit frontend. It supports both **OpenAI** (Cloud) and **Ollama** (Local Llama2).

## Prerequisites
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (Package Manager)
- An OpenAI API Key (if using Cloud)
- [Ollama](https://ollama.com/) installed and running (if using Local)

## Setup
1. Clone the repository and navigate into it.
2. Create a `.env` file and add your credentials:
   ```env
   OPENAI_API_KEY=your_openai_key_here
   LANGCHAIN_API_KEY=your_langchain_key_here
   LANGCHAIN_PROJECT=ChatBot
   ```
3. Sync the environment:
   ```bash
   uv sync
   ```

## Running the Application

This app uses a separated **Backend** and **Frontend** architecture.

### Step 1: Start the Backend (LLM Server)

Choose one of the following based on your preferred LLM:

- **Option A: Run with OpenAI (Cloud)**
  ```bash
  uv run main.py
  ```
- **Option B: Run with Ollama (Local Llama2)**
  *(Make sure you have run `ollama pull llama2` first)*
  ```bash
  uv run ollama.py
  ```

### Step 2: Start the Frontend (Streamlit)

In a **separate terminal**, run:
```bash
uv run streamlit run app.py
```

---
The application will be accessible at `http://localhost:8501`.
The FastAPI backend serves the LangChain Playground at `http://localhost:8000/chatbot/playground/`.
