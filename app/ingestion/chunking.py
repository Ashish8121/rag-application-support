from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.ingestion.load_docs import load_documents
def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_text("\n".join(documents))
    return chunks


if __name__ == "__main__":
    documents = load_documents()
    chunks = chunk_documents(documents)
    print(len(chunks))
