from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.chunks = []

    def build_index(self, chunks):
        self.chunks = chunks
        
        embeddings = self.model.encode(chunks)
        embeddings = np.array(embeddings).astype("float32")

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)

        self.index.add(embeddings)

    def search(self, query, k=3):
        query_vector = self.model.encode([query]).astype("float32")

        distances, indices = self.index.search(query_vector, k)

        results = [self.chunks[i] for i in indices[0]]

        return results