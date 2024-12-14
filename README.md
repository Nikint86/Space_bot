## Функция time_img_send 

Функция используется для автоматической отправки фото.

По умолчанию задержка 3 часа.

### Как поменять задержку?

Задержку можно изменить при помощи файла **time.env**.

`TIME_SEND = 10800`

Строка с временем в файле **time.env**. Время указывается в секундах.

`TIME = int(os.getenv("TIME_SEND"))`

Строка с использованием **time.env** в **time_img_send**.

---

## nasa_apod

Скачивает картинки дня с сайта NASA в директорию указанную в `IMAGE_DIRECTORY`

`IMAGE_DIRECTORY = Path("Ваша директория")`

Для запуска необходим API Ключ, который находится на сайте NASA.

`API_KEY = os.getenv("API_KEY")`

Указать его нужно через переменную окружения.

`API_KEY = "Ваш API Ключ с сайта NASA"`

---

## fetch_spacex_images

Скачивает фотографию с сайта Wikimedia.

Для работы необходима ваша директория.

`IMAGE_DIRECTORY = Path("Ваша директория")`

И ваша ссылка на фото.

`download_page = "Ваша ссылка"`

---

## download_epic

Скачивает EPIC фото с сайта NASA.

Для запуска необходим API Ключ, который находится на сайте NASA.

`API_KEY = os.getenv("API_KEY")`

Указать его нужно через переменную окружения.

`API_KEY = "Ваш API Ключ с сайта NASA"`

Для работы необходима ваша директория.

`IMAGE_DIRECTORY = Path("Ваша директория")`

---

## main.py

Находит разрешение файла,указанного в url.

`url = input("")`
