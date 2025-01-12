import os
import requests
from pathlib import Path
from dotenv import load_dotenv
import argparse
from save_tool import download_and_save_image


def main():
    parser = argparse.ArgumentParser(description="Скачать NASA фото")
    parser.add_argument('directory', type=str, nargs='?', help='Директория для сохранения фото.', default='images')
    args = parser.parse_args()

    image_directory = Path(args.directory)
    image_directory.mkdir(parents=True, exist_ok=True)

    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]
    num_images = 30
    payload = {"api_key": api_key, "count": f"{num_images}"}
    nasa_urls = "https://api.nasa.gov/planetary/apod"

    nasa_response = requests.get(nasa_urls, params=payload)
    nasa_response.raise_for_status()
    images_data = nasa_response.json()

    for index, item in enumerate(images_data, start=1):
        image_nasa_url = item.get("url")
        if image_nasa_url:
            print(f"Загружается изображение {index + 1}: {image_nasa_url}")
            download_and_save_image(image_nasa_url, index, image_directory)


if __name__ == '__main__':
    main()

