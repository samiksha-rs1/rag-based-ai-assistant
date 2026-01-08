import yt_dlp
import os

# Create the folder if it doesn't exist to keep your project organized
if not os.path.exists('videos'):
    os.makedirs('videos')

# The list of URLs for Videos 1-15 of the Sigma Web Dev Course
video_urls = [
    "https://www.youtube.com/watch?v=tVzUXW6siu0",
    "https://www.youtube.com/watch?v=ESLpAIvUshE",
    "https://www.youtube.com/watch?v=uF_u3ToEPHM", 
    "https://www.youtube.com/watch?v=nXba2-mgn1k",
    "https://www.youtube.com/watch?v=1DsXTSV7ip8", 
    "https://www.youtube.com/watch?v=ESnrn1kAD4E", 
    "https://www.youtube.com/watch?v=P-IofO6O1Hk",
    "https://www.youtube.com/watch?v=n06_77M6yGg", 
    "https://www.youtube.com/watch?v=fM791_H_7T4", 
    "https://www.youtube.com/watch?v=YgVfSnY7X1M", 
    "https://www.youtube.com/watch?v=2V_7zB6lBfM", 
    "https://www.youtube.com/watch?v=t_iYv_4N67w", 
    "https://www.youtube.com/watch?v=2W4o9u0K6H0", 
    "https://www.youtube.com/watch?v=9PBe5V_hH3g", 
    "https://www.youtube.com/watch?v=H9vP77G5v3A"  
]

def download_sigma_videos(urls):
    # Configuration for yt-dlp
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', # Prioritize MP4
        'outtmpl': 'videos/%(playlist_index)s_%(title)s.%(ext)s', # Number them for sequence
        'noplaylist': True, # Only download the specific video
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Starting download of {len(urls)} videos...")
        ydl.download(urls)

if __name__ == "__main__":
    download_sigma_videos(video_urls)