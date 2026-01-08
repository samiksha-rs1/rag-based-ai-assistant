# RAG AI Teaching Assistant
A high-performance, transcript-grounded Retrieval-Augmented Generation (RAG) system designed specifically for students. This assistant ensures students get accurate answers with exact video timestamps, keeping the learning experience focused and efficient.

##  Key Features
* **Transcript Grounding:** The AI answers strictly based on the course transcripts to avoid hallucinations.
* **Exact Video Citations:** Every answer identifies the specific video and the exact second where the topic is explained.
* **Strict RAG Logic:** Built-in safeguards to refuse out-of-scope questions (e.g., general knowledge or unrelated tech).
* **Automated Testing:** Includes a dedicated test runner to verify response accuracy across multiple question types.

---

## Prerequisites
Before starting, ensure you have the following installed:
* Python 3.8 or higher
* [Ollama](https://ollama.ai/) (with the `bge-m3` model pulled: `ollama pull bge-m3`)
* An OpenAI API Key
* FFmpeg (for audio conversion)

---
## Benefits of This Project
1. Accurate Navigation
Standard AI bots often give generic advice. This project acts as a Video Navigator, saving students hours of manual searching by pointing them to the exact moment the instructor explains a concept.

2. Elimination of "AI Hallucinations"
By using a Strict RAG approach, the system is forced to only use the course data. If the instructor didn't mention it, the AI won't make it up, ensuring the student only learns what is in the curriculum.

3. Accessible Learning
With the automated transcription and translation (via Whisper), the course content becomes searchable. Students can jump directly to complex topics like "Semantic Tags" or "Core Web Vitals" instantly.

4. Efficient Context Handling
Through custom chunk merging logic, the AI understands the "flow" of the lesson rather than reading isolated sentences, leading to much more human-like and helpful explanations.

## How to use this RAG AI Teaching assistant on your own data

### Step 1 - Collect your videos
Move all your video files to the `videos` folder.

### Step 2 - Convert to mp3
Convert all the video files to mp3 by running `video_to_mp3.py`.

### Step 3 - Convert mp3 to json 
Convert all the mp3 files to json by running `mp3_to_json.py`.

### Step 4 - Convert the json files to Vectors
Use the file `preprocess_json.py` to convert the json files to a dataframe with Embeddings and save it as a joblib pickle.

### Step 5 - Prompt generation and feeding to LLM
Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM.

---

## Automated Testing
To verify the system's "strictness" and accuracy, you can run the automated test suite:
```bash
python tests/rag_tester_final.py