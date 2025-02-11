# JS_quiz_bot

## О проекте:
Этот проект представляет собой бота для Telegram, который предлагает пользователю пройти 
интерактивный квиз, на тему JS, с различными уровнями сложности: новичок, продвинутый и эксперт. 
Бот использует библиотеку aiogram для обработки команд и взаимодействия с пользователем.

## Структура проекта:
+ ```handlers``` - директория содержащая ключевые файлы, 
которые обрабатывают различные
команды и события Telegram-бота. 
+ ```config_readera.py``` - хранение токена бота.
+ ```main.py``` - точка входа, код запуска бота и инициализации всех остальных модулей.
+ ```questions.py``` - Вопросы и варианты ответа, используемые ботом.

## Технологии и инструменты

- **Python:** Основной язык программирования.
- **Aiogram:** Фреймворк для создания асинхронных Telegram-ботов.

## Установка и запуск проекта:
+ Сохранить папку с проектом на своем устройстве;
+ В файле __.env__ введите токен бота;
+ Создать виртуальное окружение и запустить его:
  ```
  python -m venv venv
  ```
  ```
  venv/Scripts/activate
  ```
+ Установите зависимости из requirements.txt
  ```
  pip install -r requirements.txt
  ```
+ Запустите python-файл __main.py___