import requests
from pathlib import Path
import os
from dotenv import load_dotenv

IMAGE_DIRECTORY = Path(os.path.join("C:", "Python", "image"))
IMAGE_DIRECTORY.mkdir(parents=True, exist_ok=True)


def download_and_save_epic_image(more_epic_url, payload, new_urls):
    more_epic_response = requests.get(more_epic_url, params=payload)
    more_epic_response.raise_for_status()
    filename = IMAGE_DIRECTORY / f"{new_urls}.png"
    with open(filename, 'wb') as file:
        file.write(more_epic_response.content)


def main():
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")
    payload = {"api_key": api_key}

    urls = "https://api.nasa.gov/EPIC/api/natural/images"
    urls_response = requests.get(urls, params=payload)
    urls_response.raise_for_status()

    urls_open = urls_response.json()
    urls_textt = tuple(urls_open)

    for parsed in urls_textt:
        new_urls = parsed["image"]
        more_epic_url = f"https://api.nasa.gov/EPIC/archive/natural/2024/12/08/png/{new_urls}.png"

        download_and_save_epic_image(more_epic_url, payload, new_urls)


if __name__ == '__main__':
    main()
