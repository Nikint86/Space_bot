import requests


def download_and_save_image(image_url, index, directory):
    try:
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        filename = directory / f"spacex{index + 1}.jpg"
        with open(filename, 'wb') as file:
            file.write(image_response.content)
        print(f"Изображение {index + 1} успешно загружено: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка загрузки изображения {image_url}: {e}")
