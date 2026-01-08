import requests
import os
import json
import numpy as np
import pandas as pd
import joblib
import faiss

#embedding function 
def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    return r.json()["embeddings"]

# Reading json files 

jsons = os.listdir("newjsons")
my_dicts = []
all_embeddings = []
chunk_id = 0

for json_file in jsons:
    with open(f"newjsons/{json_file}") as f:
        content = json.load(f)

    print(f"Creating embeddings for {json_file}")

    embeddings = create_embedding([c["text"] for c in content["chunks"]])

    for i, chunk in enumerate(content["chunks"]):
        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings[i]

        my_dicts.append(chunk)
        all_embeddings.append(embeddings[i])

        chunk_id += 1



df = pd.DataFrame.from_records(my_dicts)
joblib.dump(df, "embeddings.joblib")


# Creating faiss index

embedding_matrix = np.array(all_embeddings).astype("float32")

# Normalize for cosine similarity
faiss.normalize_L2(embedding_matrix)

dim = embedding_matrix.shape[1]
index = faiss.IndexFlatIP(dim)   
index.add(embedding_matrix)

faiss.write_index(index, "faiss.index")

print("✅ embeddings.joblib and faiss.index saved successfully")


