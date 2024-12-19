import requests
import os
from pathlib import Path
from dotenv import load_dotenv

IMAGE_DIRECTORY = Path(os.path.join("C:","Python","image"))
IMAGE_DIRECTORY.mkdir(parents=True, exist_ok=True)


def main():
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")
    num_images = 30
    payload = {"api_key": api_key,
           "count" : f"{num_images}"
    }

    nasa_urls = "https://api.nasa.gov/planetary/apod"
    nasa_response = requests.get(nasa_urls, params = payload)
    nasa_response.raise_for_status()
    images_data = nasa_response.json()

    for index, item in enumerate(images_data, start=1):
        image_nasa_url = item.get("url")

        if image_nasa_url:
            print(f"Загружается изображение {index + 1}: {image_nasa_url}")
            image_response = requests.get(image_nasa_url)
            image_response.raise_for_status()
            filename = IMAGE_DIRECTORY / f"spacex{index + 1}.jpg"

            with open(filename, 'wb') as file:
                file.write(image_response.content)

if __name__ == '__main__':
    main()