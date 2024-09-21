from concurrent.futures import ThreadPoolExecutor
from threading import Thread

import requests
import yt_dlp
import time


devara_video_urls = [
    'https://www.youtube.com/watch?v=5cx7rvMvAWo',
    'https://www.youtube.com/watch?v=FUGcRzAFAD8&t=1s',
    'https://www.youtube.com/watch?v=byEjl2kJGK0',
    'https://www.youtube.com/watch?v=NcCYq3bvlJM&t=1s'
]


def download_video(url):
    ydl_opts = {
        'outtmpl': r'C:\Users\ramun\Downloads\devara/%(title)s.%(ext)s',  # Downloads to the Downloads folder
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

start_time = time.time()

with ThreadPoolExecutor() as executor:
    results = [executor.submit(download_video, video_url) for video_url in devara_video_urls]


finish_time = time.time()

print(f'Time taken to download the video: {round(finish_time-start_time, 2)} seconds')