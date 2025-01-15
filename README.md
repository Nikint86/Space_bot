## Установка библиотек

В файле requirements.txt указанны библиотеки, необходимые для работы скриптов.

### Как установить?

Введите в Bash команду:

```pip install -r requirements.txt```

---

## Функция time_img_send

Функция используется для автоматической отправки фото.

По умолчанию задержка 3 часа.

### Переменные окружения:

`token = os.environ["TG_BOT_TOKEN"]`

Токен зарегистрированного бота

`chat_id = os.environ["GROUP_TG_CHAT_ID"]`

Чат ID вашей группы или пользователя, которому Вы хотите отправить сообщение.

`time = int(os.environ["BOT_TIMER"])`

Задержка, с которой бот отправляет сообщение.

По умолчанию задержка 3 часа.

`TG_BOT_TOKEN, GROUP_TG_CHAT_ID, BOT_TIMER` Прописываются в файле .env

### Как поменять задержку?

Задержку можно изменить при помощи переменной окружения `BOT_TIMER`

`time = int(os.getenv["BOT_TIMER"])`

### Как запустить?

```python time_img_send```

### Как проверить?

Бот должен отправить картинку указанную в директории в чат, указанный в `chat_id`

---

## download_nasa_apod

Скачивает картинки дня с сайта NASA в директорию.

Версия Python 3.12

### Директория
Директория указывается при запуске программы.

По умолчанию images

### Переменные окружения:

Для запуска необходим API Ключ, который находится на сайте NASA.

`api_key = os.environ["NASA_API_KEY"]`

Указать его нужно через переменную окружения.

`API_KEY = "Ваш API Ключ с сайта NASA"`

Внести его необходимо через файл .env который необходимо создать.

### Как запустить?

```python nasa_apod```

### Как проверить?

Скачивает фотографии дня с сайта NASA в директорию указанную пользователем(по умолчанию images).

---

## download_wikimedia_image

Скачивает фотографию с сайта Wikimedia.

Версия Python 3.12

Для работы необходима ваша директория.

Директория указывается при запуске программы.

По умолчанию images.

И ваша ссылка на фото.

`download_page = "Ваша ссылка"`

### Как запустить?

```python wikimedia_img```

### Как проверить?

Скрипт скачает фотографию с сайта Wikimedia в директорию.

---

## download_epic_nasa_image

Скачивает EPIC фото с сайта NASA.

Версия Python 3.12

Для запуска необходим API Ключ, который находится на сайте NASA.

`api_key = os.environ["NASA_API_KEY"]`

Указать его нужно через переменную окружения.

`API_KEY = "Ваш API Ключ с сайта NASA"`

Для работы необходима ваша директория, которая указывается при запуске программы.

По умолчанию images.

`NASA_API_KEY` указывается в файле .env

### Как запустить?

```python download_epic```

### Как проверить?

Скачает EPIC фото с сайта NASA в директорию, указанную пользователем.

---

