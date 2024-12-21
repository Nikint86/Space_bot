## Функция time_img_send 

Функция используется для автоматической отправки фото.

По умолчанию задержка 3 часа.

### Для cкрипта необходимо:

`$ python -m pip install dotenv==1.0.1`

Версия Python 3.12

### Переменные окружения:

`token = os.getenv("TG_BOT_TOKEN")`

Токен зарегистрированного бота

`chat_id = os.getenv("GROUP_TG_CHAT_ID")`

Чат ID вашей группы или пользователя, которому Вы хотите отправить сообщение.

`TIME = int(os.getenv("TIME_SEND"))`

Задержка, с которой бот отправляет сообщение.

### Как поменять задержку?

Задержку можно изменить при помощи файла **time.env**.

`TIME_SEND = 10800`

Строка с временем в файле **time.env**. Время указывается в секундах.

`TIME = int(os.getenv("TIME_SEND"))`

Строка с использованием **time.env** в **time_img_send**.

### Как запустить?

`python time_img_send`

### Как проверить?

Бот должен отправить картинку указанную в директории в чат, указанный в `chat_id`

---

## nasa_apod

Скачивает картинки дня с сайта NASA в директорию указанную в `IMAGE_DIRECTORY`

### Для cкрипта необходимо:

`$ python -m pip install requests==2.32.3`

`$ python -m pip install pathlib==1.0.1`

Версия Python 3.12

### Директория
`IMAGE_DIRECTORY = Path("Ваша директория")`

### Переменные окружения:

Для запуска необходим API Ключ, который находится на сайте NASA.

`API_KEY = os.getenv("API_KEY")`

Указать его нужно через переменную окружения.

`API_KEY = "Ваш API Ключ с сайта NASA"`

### Как запустить?

`python nasa_apod`

### Как проверить?

Скачивает фотографии дня с сайта NASA в директорию указанную в IMAGE_DIRECTORY.

---

## fetch_spacex_images

Скачивает фотографию с сайта Wikimedia.

### Для cкрипта необходимо:

`$ python -m pip install requests==2.32.3`

`$ python -m pip install pathlib==1.0.1`

Версия Python 3.12

Для работы необходима ваша директория.

`IMAGE_DIRECTORY = Path("Ваша директория")`

И ваша ссылка на фото.

`download_page = "Ваша ссылка"`

### Как запустить?

`python fetch_spacex_images`

### Как проверить?

Скрипт скачает фотографию с сайта Wikimedia в директорию, указанную в `IMAGE_DIRECTORY`

---

## download_epic

Скачивает EPIC фото с сайта NASA.

### Для cкрипта необходимо:

`$ python -m pip install requests==2.32.3`

`$ python -m pip install pathlib==1.0.1`

Версия Python 3.12

Для запуска необходим API Ключ, который находится на сайте NASA.

`API_KEY = os.getenv("API_KEY")`

Указать его нужно через переменную окружения.

`API_KEY = "Ваш API Ключ с сайта NASA"`

Для работы необходима ваша директория.

`IMAGE_DIRECTORY = Path("Ваша директория")`

### Как запустить?

`python download_epic`

### Как проверить?

Скачает EPIC фото с сайта NASA в директорию, указанную в IMAGE_DIRECTORY.

---

## main.py

Находит разрешение файла указанного в url.

### Для скрипта необходимо:

`$ python -m pip install argparse=1.4.0`

### Как указать ссылку на файл?

`python main.py Ваша сслыка`

### Как проверить?

Укажет разрешение файла.

Пример: `.json` или `.txt`