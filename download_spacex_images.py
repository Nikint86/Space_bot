import requests
from pathlib import Path
import argparse
from save_tool import download_and_save_image


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Скачать фото с последнего запуска spacex.")
    parser.add_argument('directory',
                        type=str,
                        nargs='?',
                        help='Директория для сохранения фото.',
                        default='images')

    args = parser.parse_args()
    image_directory = Path(args.directory)
    image_directory.mkdir(parents=True, exist_ok=True)

    spacex_url = "https://api.spacexdata.com/v5/launches/latest"

    response = requests.get(spacex_url)
    response.raise_for_status()

    response_spacex = response.json()
    spacex_links = response_spacex["links"]["flickr"]["original"]

    for original_number, original in enumerate(spacex_links, start=1):
        print(f"Загружается изображение: {original}")
        download_and_save_image(original, image_directory)
