import yt_dlp
import os

playlist_url = "https://www.youtube.com/playlist?list=PL_UgZUhvA-uZZDdG1YN1mBNd3kE5i2MOt"

ydl_opts = {
    # Download best audio only
    "format": "bestaudio/best",

    # Output folder + safe names
    "outtmpl": "mp3/%(playlist_title)s/%(playlist_index)02d - %(title)s.%(ext)s",
    "restrictfilenames": True,

    # Convert to MP3 after download
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }
    ],

    # YouTube blocking fixes
    "extractor_args": {
        "youtube": {
            "player_client": ["android"]
        }
    },

    "quiet": False
}

os.makedirs("mp3", exist_ok=True)

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
