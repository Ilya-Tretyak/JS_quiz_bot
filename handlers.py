from aiogram import types, Router, F
from aiogram.filters.command import Command

import kb
from state import StatusTest
from questions import questions

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🎯 Выбери уровень сложности:", reply_markup=kb.chooce_level)
    

@router.message(F.text=="👶Новичок")
async def send_quiz(message: types.Message):
    current_question = 0
    correct_answer = 0

    while True:
        question = questions[current_question]

        kb = []
        for option in question['answer_options']:
            kb.append([types.KeyboardButton(text=option)])
        
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer(question['text'], reply_markup=keyboard)

        user_answer = None
        while user_answer not in question['answer_options']:
            user_answer = await message.answer("Пожалуйста, выберите один из вариантов ответа и напишите его.")
        
        if user_answer == question['options'][question['right_answer']]:
            correct_answer += 1
        
        current_question += 1
        if current_question >= len(questions):
            await message.answer(f"Тест завершен!\nВы правильно ответили на {correct_answer} вопросов.")
            break
        