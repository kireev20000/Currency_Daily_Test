# Название Проекта

---

Краткое Описание

---
 
***
## Особенности проекта
- Отрабатываю полученные знание на практике.
- Использую по возможности самые современные технологии.

## Стек
- Python 3.10
- Selenium 4.3.0
- Beautiful Soup4  4.11.1
- undetected-chromedriver 2.1.1 
- Openpyxl 3.10
- tqdm 4.64
___

## Техническое задание или Идея
***

## Текущий прогресс
- приложение для ведения блога на Django 4 (Done);
- веб-сайт по управлению визуальными закладками (Done);

### Особенности приложения с визуальными закладками
- использование JavaScript вместе с Django;
- формирование букмарклета JavaScript;
- генерирование миниатюр изображений с помощью easy-thumbnails;
- реализация асинхронных HTTP-запросов с помощью JavaScript
и Django;
- разработка бесконечной постраничной прокрутки
- разработана системы подписки;
- создание приложения потока активности;
- ведение подсчета просмотров изображений с помощью хранилища
Redis;
- создание рейтинга самых просматриваемых изображений с помощью
хранилища Redis

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone 
```
***- Установите зависимости из файла requirements.txt:***
```
pip install -r requirements.txt
```

***- Примените миграции:***
```
python manage.py migrate
```

### Запускаем внешние БД в докере:
Установить и настроить PostgreSQL и Redis в докере

```
docker pull redis
docker run -it --rm --name redis -p 6379:6379 redis
```
***- В папке с файлом manage.py выполните команду для запуска локально:***
```
python manage.py runserver
```
Cоздать и заполнить .env файл в корневой директории
```
SECRET_KEY = "ваш_ключ_Django"
```


## Об авторе <a id=7></a>

Киреев Александр Олегович  
Python-разработчик (Backend)  
E-mail: kireev20000@yandex.ru
Telegram: @kireev20000

# Инструкция по запуску