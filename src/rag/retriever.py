from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from nlp.extract import psych_kb  # Import KB from extract.py

embed_model = SentenceTransformer('all-MiniLM-L6-v2')

knowledge = list(psych_kb.values())
embeddings = embed_model.encode(knowledge, convert_to_numpy=True)
dim = embeddings.shape[1]

index = faiss.IndexFlatL2(dim)
index.add(embeddings)

def retrieve_from_faiss(symbols):
    queries = [psych_kb[s] for s in symbols if s in psych_kb]
    if not queries:
        return "No knowledge found"
    query_emb = embed_model.encode(queries, convert_to_numpy=True)
    D, I = index.search(query_emb, k=1)
    return " | ".join([knowledge[i[0]] for i in I])
