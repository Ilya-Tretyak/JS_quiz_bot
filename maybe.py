```python
import random
from aiogram import Bot, Dispatcher, executor, types

# Инициализация бота и диспетчера
API_TOKEN = 'YOUR_API_TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Список вопросов и ответов
questions = [
    {
        "question": "Какой город является столицей России?",
        "options": ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург"],
        "correct_answer": "Москва"
    },
    {
        "question": "Какое самое высокое здание в мире?",
        "options": ["Эйфелева башня", "Бурдж-Халифа", "Останкинская телебашня", "Си-Эн Тауэр"],
        "correct_answer": "Бурдж-Халифа"
    },
    {
        "question": "Кто автор книги 'Война и мир'?",
        "options": ["Лев Толстой", "Федор Достоевский", "Антон Чехов", "Александр Пушкин"],
        "correct_answer": "Лев Толстой"
    }
]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я - квиз-бот. Готов ответить на твои вопросы?")

@dp.message_handler(commands=['quiz'])
async def start_quiz(message: types.Message):
    await message.reply("Давай начнем квиз!\n")
    for question in questions:
        await message.answer(question["question"])
        options = question["options"]
        correct_answer = question["correct_answer"]
        
        user_answer = await bot.send_message(message.chat.id, "Выбери вариант ответа:")
        for option in options:
            await bot.send_message(message.chat.id, option)
        
        response = await bot.send_message(message.chat.id, "Твой выбор: ")
        await bot.register_next_step_handler(user_answer, add_answer)

def add_answer(message: types.Message, correct_answer: str):
    if message.text == correct_answer:
        await bot.send_message(message.chat.id, "Правильный ответ!")
    else:
        await bot.send_message(message.chat.id, "Неверный ответ. Правильный ответ: " + correct_answer)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
```

Этот код создает телеграм-бота на базе Aiogram 3.15, который проводит квиз. Вопросы, варианты ответов и правильные ответы берутся из списка. Бот отправляет вопросы пользователю, получает ответы и сообщает, правильный ли это ответ.