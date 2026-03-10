# RAG Customer Support AI (FastAPI + FAISS + Groq)

A **Retrieval-Augmented Generation (RAG) application** that allows users to ask questions about PDF documents.
The system retrieves relevant document chunks using a **vector database (FAISS)** and generates answers using **Groq Llama3**.

This project demonstrates a **production-style RAG pipeline** built with FastAPI and modern LLM tooling.

---

# Features

* FastAPI API for user queries
* PDF document ingestion
* Document chunking
* Semantic embeddings using Sentence Transformers
* FAISS vector database for similarity search
* Groq LLM (Llama3) for answer generation
* Environment variable management using `.env`
* Modular and scalable project structure

---

# Architecture

User Question
↓
FastAPI API (`/ask`)
↓
RAG Pipeline
↓
Retrieve relevant document chunks (FAISS)
↓
Send context + question to Groq LLM
↓
Generated answer returned to user

---

# Project Structure

```
rag_app
│
├── app
│   ├── api
│   │   └── main.py
│   │
│   ├── core
│   │   └── rag_pipeline.py
│   │
│   ├── ingestion
│   │   ├── load_docs.py
│   │   └── chunking.py
│   │
│   └── retriever
│       ├── vector_store.py
│       └── build_index.py
│
├── data
│   └── raw
│       └── pdf_documents
│
├── .env.example
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/rag-customer-support-ai.git
cd rag-customer-support-ai
```

Create a virtual environment:

```
python -m venv .venv
```

Activate environment:

Windows

```
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

# Add Documents

Place your PDF files inside:

```
data/raw/
```

Example:

```
data/raw/microsoft_history.pdf
```

---

# Run the Application

Start the FastAPI server:

```
uvicorn app.api.main:app --reload
```

API will start at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# Example Request

POST request:

```
POST /ask
```

Body:

```
{
  "question": "Who founded Microsoft?"
}
```

Response:

```
{
  "answer": "Microsoft was founded by Bill Gates and Paul Allen in 1975."
}
```

---

# Tech Stack

* Python
* FastAPI
* FAISS
* Sentence Transformers
* Groq LLM (openai)
* LangChain text splitters
* Pydantic

---

# Author

Ashish Kumar

---

# License

MIT License
