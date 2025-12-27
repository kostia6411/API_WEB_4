import os
import requests
from pathlib import Path
from bs4 import BeautifulSoup


def download_text(artist_names, full_title, url_lyrics):
    text_path = f"songs/{artist_names}/lyrics"
    os.makedirs(text_path, exist_ok=True)
    lyrics_name = f"{full_title}.txt"
    lyrics_path = os.path.join(text_path, lyrics_name)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 YaBrowser/25.7.0.0 Safari/537.36",
    }
    response = requests.get(url_lyrics, headers=headers)
    response.raise_for_status() 
    bs = BeautifulSoup(response.text,"html.parser")
    temp = bs.select_one('.Lyrics__Container-sc-68a46031-1')
    temp.select_one(".LyricsHeader__Container-sc-6f4ef545-1").decompose()
    lyrics = temp.get_text(separator="\n")
    with open(lyrics_path, 'w', encoding="UTF-8") as file:
        file.write(lyrics)


def download_img(artist_names, image_url, full_title):
    folder_path = f"songs/{artist_names}/images"
    os.makedirs(folder_path, exist_ok=True)
    img_extention = Path(image_url).suffix
    img_name = f"{full_title}{img_extention}"
    file_path = os.path.join(folder_path, img_name)
    response = requests.get(image_url)
    response.raise_for_status() 
    with open(file_path, 'wb') as file:
        file.write(response.content)