from app.ingestion.load_docs import load_documents
from app.ingestion.chunking import chunk_documents
from app.retriever.vector_store import VectorStore
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()   # loads .env file


class RAGPipeline:

    def __init__(self):

        documents = load_documents()
        chunks = chunk_documents(documents)

        self.store = VectorStore()
        self.store.build_index(chunks)

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def get_answer(self, query):

        results = self.store.search(query)
        context = "\n".join(results)

        prompt = f"""
        Answer the question using the context below.

        Context:
        {context}

        Question:
        {query}
        """

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content