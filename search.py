import argparse
import os
import requests
from dotenv import load_dotenv
from tools import download_img, download_text


def song_search(name, api_key):
    url = f"https://api.genius.com/search"
    params = {
        "q": name
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 YaBrowser/25.7.0.0 Safari/537.36",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status() 
    songs = response.json()["response"]["hits"]
    for song in songs:
        artist_names = song["result"]["artist_names"]
        full_title = song["result"]["full_title"]
        release_date = song["result"]["release_date_for_display"]
        image_url = song["result"]["header_image_thumbnail_url"]
        url_lyrics = song["result"]["url"]
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
    parser = argparse.ArgumentParser(description="Позволяет получать информацию и скачивать обложки, текст песни по имени артиста или названию песни")
    parser.add_argument("-n", "--name", type=str, help="Введите имя исполнителя или название песни", required=False, default="Sia")
    args = parser.parse_args()
    song_search(args.name, api_key)


if __name__ == '__main__':
    main()