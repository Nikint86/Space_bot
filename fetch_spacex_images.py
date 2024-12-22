from pathlib import Path
import argparse
from save_tool import download_and_save_image


def open_wikipedia():
    wikipedia_page = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    return wikipedia_page


def main(image_directory):
    image_directory.mkdir(parents=True, exist_ok=True)
    filename = image_directory / "hubble.jpeg"
    download_and_save_image(open_wikipedia(), 0, image_directory)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Скачать фото с сайта Wikipedia")
    parser.add_argument('directory', type=str, help='Директория для сохранения фото.')
    args = parser.parse_args()

    image_directory = Path(args.directory)
    main(image_directory)


