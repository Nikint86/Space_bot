import requests
from pathlib import Path
import os
from dotenv import load_dotenv

IMAGE_DIRECTORY = Path("C:/Python/image")
IMAGE_DIRECTORY.mkdir(parents=True, exist_ok=True)

load_dotenv()

API_KEY = os.getenv("API_KEY")



def image_setup():
    download_page = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    filename = IMAGE_DIRECTORY / "hubble.jpeg"
    response = requests.get(download_page)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def more_nasa_side():

    num_images = 30
    payload = {"api_key": API_KEY,
           "count" : f"{num_images}"
    }

    nasa_urls = "https://api.nasa.gov/planetary/apod"
    nasa_response = requests.get(nasa_urls, params = payload)
    nasa_response.raise_for_status()
    images_data = nasa_response.json()

    for index, item in enumerate(images_data):
        image_nasa_url = item.get("url")

        if image_nasa_url:
            print(f"Загружается изображение {index + 1}: {image_nasa_url}")
            image_response = requests.get(image_nasa_url)
            image_response.raise_for_status()
            filename = IMAGE_DIRECTORY / f"nasa_image_{index + 1}.jpg"

            with open(filename, 'wb') as file:
                file.write(image_response.content)


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


def more_ep_urls():
    payload = {"api_key": API_KEY

                }
    urls = "https://api.nasa.gov/EPIC/api/natural/images"
    urls_response = requests.get(urls, params = payload)
    urls_response.raise_for_status()
    urls_json = urls_response.json()
    urls_textt = tuple(urls_json)
    parsed = urls_textt[0]

    for parsed in urls_textt:
        new_urls = parsed["image"]
        more_epic_url = f"https://api.nasa.gov/EPIC/archive/natural/2024/12/08/png/{new_urls}.png"
        more_epic_urlll = requests.get(more_epic_url, params = payload)
        more_epic_urlll.raise_for_status()

        filename = IMAGE_DIRECTORY / f"{new_urls}.png"
        with open(filename, 'wb') as file:
            file.write(more_epic_urlll.content)


def nasa_epic():
    payload = {"api_key": API_KEY

    }

    nasa_img_epic = "https://api.nasa.gov/EPIC/archive/natural/2024/12/08/png/epic_1b_20241208010437.png"
    epic_img_response = requests.get(nasa_img_epic, params = payload)
    epic_img_response.raise_for_status()

    filename = IMAGE_DIRECTORY / "epic.jpg"
    with open(filename, 'wb') as file:
        file.write(epic_img_response.content)


def find_jpeg():
    url = input("")
    splited_url = os.path.splitext(url)
    print("Разрешение файла:", splited_url[1])

#more_ep_urls()
#more_nasa_side()
#nasa_epic()
#find_jpeg()
#image_setup()
#download_spacex_images()
