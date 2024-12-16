import os
import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Определяет разрешение файла.'
    )
    parser.add_argument('url', help='Ваш URL', type=str)
    args = parser.parse_args()
    print(args.url)
    print(type(args.url))
    splited_url = os.path.splitext(args.url)
    print("Разрешение файла:", splited_url[1])

if __name__ == '__main__':
    main()