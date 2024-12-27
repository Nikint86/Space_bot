import random
import telegram
import os
from dotenv import load_dotenv
from time import sleep
import argparse

def main():
    load_dotenv()
    token = os.environ["TG_BOT_TOKEN"]
    chat_id = os.environ["GROUP_TG_CHAT_ID"]
    time = int(os.environ["BOT_TIMER"])
    parser = argparse.ArgumentParser(description="Отправить случайную картинку в группу Telegram")
    parser.add_argument('directory', type=str, help='Директория с картинками.')
    args = parser.parse_args()
    img_directory = os.listdir(args.directory)
    bot = telegram.Bot(token=token)
    while True:
        random.shuffle(img_directory)
        for rand_choice in img_directory:
            document_path = os.path.join(args.directory, rand_choice)
            with open(document_path, "rb") as document_file:
                bot.send_document(chat_id=chat_id, document=document_file)
            sleep(time)


if __name__ == '__main__':
    main()

