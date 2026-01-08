import pandas as pd 
import numpy as np 
import joblib 
import requests
import faiss
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    embedding = r.json()["embeddings"] 
    return embedding


def inference(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are the Sigma Course Technical Expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
        frequency_penalty=0.5,
        max_tokens=400
    )

    return {
        "response": response.choices[0].message.content
    }


df = joblib.load('embeddings.joblib')
index = faiss.read_index("faiss.index")


incoming_query = input("Ask a Question: ")
question_embedding = create_embedding([incoming_query])[0] 

query_vector = np.array([question_embedding]).astype("float32")
faiss.normalize_L2(query_vector)

top_results =5
scores, indices = index.search(query_vector, top_results)

max_indx = indices[0]
new_df = df.iloc[max_indx] 


prompt = f'''I am teaching web development in my Sigma web development course. Here are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:

{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}
---------------------------------
"{incoming_query}"
- User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course.

- Politely refuse the questions which are not related to web development course.

-Stop providing external definitions for out-of-scope technical terms (if any word is just appeared 1-2 times in the course and no further explantion on that topic given by the instructor) if they aren't explained in the transcript.eg:- If a technical term is mentioned but not explained, state that it is mentioned in [Video X] but not explained in detail in this course. Do NOT provide external definitions.

# - Give deterministic responses of the questions being asked by the student
'''



with open("prompt.txt", "w", encoding="utf-8") as f:
    f.write(prompt)

response = inference(prompt)["response"]
print(response)

with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response)
