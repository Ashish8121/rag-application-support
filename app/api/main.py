from fastapi import FastAPI
from pydantic import BaseModel
from app.core.rag_pipeline import RAGPipeline

app = FastAPI(title='RAG Customer Support App')

class UserQuery(BaseModel):
    question: str

rag_pipeline = RAGPipeline()

@app.post('/ask')
def ask_question(query: UserQuery):
    user_input = query.question
    reply = rag_pipeline.get_answer(user_input)
    return {'answer': reply}