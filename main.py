from pathlib import Path
import os
from dotenv import load_dotenv

IMAGE_DIRECTORY = Path("C:/Python/image")
IMAGE_DIRECTORY.mkdir(parents=True, exist_ok=True)

load_dotenv()

API_KEY = os.getenv("API_KEY")


def find_jpeg():
    url = input("")
    splited_url = os.path.splitext(url)
    print("Разрешение файла:", splited_url[1])


