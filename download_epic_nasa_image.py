import os
import requests
from pathlib import Path
from dotenv import load_dotenv
import argparse
from save_tool import download_and_save_image


def main():
    parser = argparse.ArgumentParser(description="Скачать EPIC с сайта NASA")
    parser.add_argument('directory',
                        type=str,
                        nargs='?',
                        help='Директория для сохранения EPIC файлов',
                        default='images')
    args = parser.parse_args()

    image_directory = Path(args.directory)
    image_directory.mkdir(parents=True, exist_ok=True)
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]
    payload = {"api_key": api_key}
    url = "https://api.nasa.gov/EPIC/api/natural/images"

    url_response = requests.get(url, params=payload)
    url_response.raise_for_status()
    url_open = url_response.json()

    for index, parsed in enumerate(url_open, start=1):
        new_url = parsed["image"]
        more_epic_url = f"https://api.nasa.gov/EPIC/archive/natural/2024/12/08/png/{new_url}.png"

        download_and_save_image(more_epic_url, image_directory)


if __name__ == '__main__':
    main()
