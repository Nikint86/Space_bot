import requests
from pathlib import Path


IMAGE_DIRECTORY = Path("C:/Python/image")
IMAGE_DIRECTORY.mkdir(parents=True, exist_ok=True)


def open_wikipedia():
    wikipedia_page = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    return wikipedia_page


def main(wikipedia_page):
    filename = IMAGE_DIRECTORY / "hubble.jpeg"
    response = requests.get(wikipedia_page)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


main(wikipedia_page= open_wikipedia())