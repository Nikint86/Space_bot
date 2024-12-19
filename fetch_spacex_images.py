import requests
from pathlib import Path
import os

IMAGE_DIRECTORY = Path(os.path.join("C:","Python","image"))
IMAGE_DIRECTORY.mkdir(parents=True, exist_ok=True)

def open_wikipedia():
    wikipedia_page = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    return wikipedia_page

def download_image(wikipedia_page, filename):
    response = requests.get(wikipedia_page)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)

def main(wikipedia_page):
    filename = IMAGE_DIRECTORY / "hubble.jpeg"
    download_image(wikipedia_page, filename)

if __name__ == '__main__':
    main(wikipedia_page=open_wikipedia())
