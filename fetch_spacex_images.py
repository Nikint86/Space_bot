import requests
from pathlib import Path


IMAGE_DIRECTORY = Path("C:/Python/image")
IMAGE_DIRECTORY.mkdir(parents=True, exist_ok=True)


def image_setup():
    download_page = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    filename = IMAGE_DIRECTORY / "hubble.jpeg"
    response = requests.get(download_page)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


image_setup()