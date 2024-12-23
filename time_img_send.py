import random
import telegram
import os
from dotenv import load_dotenv
from time import sleep
import argparse

def main(image_directory):
    load_dotenv()
    token = os.environ["TG_BOT_TOKEN"]
    chat_id = os.environ["GROUP_TG_CHAT_ID"]
    time = int(os.environ["BOT_TIMER"])
    open_directory = os.listdir(image_directory)

    while True:
        random.shuffle(open_directory)
        for rand_choice in open_directory:
            bot = telegram.Bot(token=token)
            document_path = os.path.join(image_directory, rand_choice)
            with open(document_path, "rb") as document_file:
                bot.send_document(chat_id=chat_id, document=document_file)
            sleep(time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Send random images to Telegram group")
    parser.add_argument('directory', type=str, help='Directory containing images')
    args = parser.parse_args()
    main(args.directory)
