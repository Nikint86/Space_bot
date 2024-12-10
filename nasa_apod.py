import requests
from pathlib import Path
import os
from dotenv import load_dotenv

IMAGE_DIRECTORY = Path("C:/Python/image")
IMAGE_DIRECTORY.mkdir(parents=True, exist_ok=True)

load_dotenv()

API_KEY = os.getenv("API_KEY")

def download_spacex_images():
    spacex_url = "https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384"
    response = requests.get(spacex_url)
    response.raise_for_status()

    restext = response.json()
    spacex_links = restext["links"]["flickr"]["original"]


    for original_number, original in enumerate(spacex_links):
        print(f"Загружается изображение {original_number + 1}: {original}")
        response = requests.get(original)
        response.raise_for_status()


        filename = IMAGE_DIRECTORY / f"space_x_{original_number + 1}.jpg"
        with open(filename, 'wb') as file:
         file.write(response.content)

download_spacex_images()