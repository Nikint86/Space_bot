import random
import telegram
import os
from dotenv import load_dotenv
from time import sleep


DOCUMENT = os.listdir(os.path.join("C:","Python","image"))


def main():
    load_dotenv()
    token = os.getenv("TG_BOT_TOKEN")
    chat_id = os.getenv("GROUP_TG_CHAT_ID")
    time = int(os.getenv("BOT_TIMER"))
    while True:
        random.shuffle(DOCUMENT)
        for rand_choice in DOCUMENT:
            bot = telegram.Bot(token=token)
            with open(os.path.join("C:", "Python", "image" f"{rand_choice}", "rb")) as document_file:
                bot.send_document(chat_id=chat_id, document=document_file)
            sleep(time)

main()