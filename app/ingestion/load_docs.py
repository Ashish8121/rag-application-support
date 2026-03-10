from pypdf import PdfReader
import os 

DATA_PATH = 'data/raw'
def load_documents():
    docs = []
    for file in os.listdir(DATA_PATH):
        if file.endswith('.pdf'):
            reader = PdfReader(os.path.join(DATA_PATH, file))
            for page in reader.pages:
                docs.append(page.extract_text())
    return docs

if __name__=="__main__":
    documents = load_documents()