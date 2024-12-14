import telegram
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def main():
    bot = telegram.Bot(token= TOKEN)
    bot.send_document(chat_id= CHAT_ID, document=open('C:/Python/image/hubble.jpeg','rb'))

main()