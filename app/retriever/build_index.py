from app.ingestion.load_docs import load_documents
from app.ingestion.chunking import chunk_documents
from app.retriever.vector_store import VectorStore
# Load documents
documents = load_documents()

# Create chunks
chunks = chunk_documents(documents)

# Build vector database
store = VectorStore()
store.build_index(chunks)

print("Vector database created with", len(chunks), "chunks")