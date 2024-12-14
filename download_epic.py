import requests
from pathlib import Path
import os
from dotenv import load_dotenv


IMAGE_DIRECTORY = Path("C:/Python/image")
IMAGE_DIRECTORY.mkdir(parents=True, exist_ok=True)

load_dotenv()

API_KEY = os.getenv("API_KEY")


def more_ep_urls():
    payload = {"api_key": API_KEY

                }
    urls = "https://api.nasa.gov/EPIC/api/natural/images"
    urls_response = requests.get(urls, params = payload)
    urls_response.raise_for_status()
    urls_json = urls_response.json()
    urls_textt = tuple(urls_json)

    for parsed in urls_textt:
        new_urls = parsed["image"]
        more_epic_url = f"https://api.nasa.gov/EPIC/archive/natural/2024/12/08/png/{new_urls}.png"
        more_epic_urlll = requests.get(more_epic_url, params = payload)
        more_epic_urlll.raise_for_status()

        filename = IMAGE_DIRECTORY / f"{new_urls}.png"
        with open(filename, 'wb') as file:
            file.write(more_epic_urlll.content)

more_ep_urls()