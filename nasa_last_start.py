import requests
from pathlib import Path
import argparse

def download_image(image_url, image_number, image_directory):
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        filename = image_directory / f"space_nasa_{image_number}.jpg"
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Изображение {image_number} успешно загружено: {filename}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Скачать фото с последнего запуска NASA.")
    parser.add_argument('directory', type=str, help='Директория для сохранения фото.')

    args = parser.parse_args()
    image_directory = Path(args.directory)
    image_directory.mkdir(parents=True, exist_ok=True)

    spacex_url = "https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384"

    response = requests.get(spacex_url)
    response.raise_for_status()

    restext = response.json()
    spacex_links = restext["links"]["flickr"]["original"]

    for original_number, original in enumerate(spacex_links, start=1):
        print(f"Загружается изображение {original_number}: {original}")
        download_image(original, original_number, image_directory)

