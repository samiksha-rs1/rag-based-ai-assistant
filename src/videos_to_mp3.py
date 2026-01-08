import os
import subprocess

os.makedirs("audios", exist_ok=True)

for file in os.listdir("videos"):
    if not file.lower().endswith((".mp4", ".mkv", ".avi", ".mov")):
        continue

    name, _ = os.path.splitext(file)   # removes extension safely
    print("Converting:", name)

    subprocess.run(["ffmpeg", "-y", "-i", f"videos/{file}",f"audios/{name}.mp3" ])
