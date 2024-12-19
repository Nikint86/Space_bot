import requests
from pathlib import Path
import os

IMAGE_DIRECTORY = Path(os.path.join("C:", "Python", "image"))
IMAGE_DIRECTORY.mkdir(parents=True, exist_ok=True)

def download_image(image_url, image_number):
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        filename = IMAGE_DIRECTORY / f"space_x_{image_number}.jpg"
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Изображение {image_number} успешно загружено: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке изображения {image_url}: {e}")


def main():
    spacex_url = "https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384"
    response = requests.get(spacex_url)
    response.raise_for_status()
    restext = response.json()
    spacex_links = restext["links"]["flickr"]["original"]

    for original_number, original in enumerate(spacex_links, start=1):
        print(f"Загружается изображение {original_number}: {original}")
        download_image(original, original_number)

if __name__ == '__main__':
    main()

