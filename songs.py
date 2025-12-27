import argparse
import os
import requests
from dotenv import load_dotenv
from tools import download_img, download_text


def get_song(song_id, api_key):
    url = f"https://api.genius.com/songs/{song_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 YaBrowser/25.7.0.0 Safari/537.36",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status() 
    song = response.json()["response"]["song"]
    artist_names = song["artist_names"]
    full_title = song["full_title"]
    release_date = song["release_date_for_display"]
    image_url = song["header_image_thumbnail_url"]
    url_lyrics = song["url"]
    print(f"Музыкант: {artist_names}") 
    print(f"Название: {full_title}")
    print(f"Дата выхода: {release_date}")
    print(f"ссылка на изображение: {image_url}")
    print(f"Ссылка на текст: {url_lyrics}\n")
    download_img(artist_names, image_url, full_title)
    download_text(artist_names, full_title, url_lyrics)


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    parser = argparse.ArgumentParser(description="Позволяет получать информацию и скачивать обложки, текст песни по id")
    parser.add_argument("-id", "--song_id", type=str, help="Введите id песни", required=False, default="378195")
    args = parser.parse_args()
    get_song(args.song_id, api_key)


if __name__ == '__main__':
    main()