import requests


def download_and_save_image(image_url, index, directory):
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        filename = directory / f"saved_image{index + 1}.jpg"
        with open(filename, 'wb') as file:
            file.write(image_response.content)
        print(f"Изображение {index + 1} успешно загружено: {filename}")