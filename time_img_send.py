import random

import telegram
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TIME = int(os.getenv("TIME_SEND"))
DOCUMENT = os.listdir("C:/Python/image/")


def main():
    while True:
        for rand_choice in DOCUMENT:
            random.shuffle(DOCUMENT)
            rand_choice = random.choice(DOCUMENT)
            bot = telegram.Bot(token= TOKEN)
            bot.send_document(chat_id= CHAT_ID, document=open(f'C:/Python/image/{rand_choice}','rb'))
            sleep(TIME)
main()