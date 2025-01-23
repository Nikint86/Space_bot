import requests


def download_and_save_image(image_url, directory):
    image_response = requests.get(image_url, stream=True)
    image_response.raise_for_status()
    filepath = directory / f"saved_image.jpg"
    with open(filepath, 'wb') as file:
       file.write(image_response.content)
    print(f"Изображение успешно загружено: {filepath}")
