import os


def find_jpeg():
    url = input("")
    splited_url = os.path.splitext(url)
    print("Разрешение файла:", splited_url[1])


find_jpeg()