from aiogram import types, Router, F
from aiogram.filters.command import Command

import kb
from questions import questions

router = Router()


class QuizState:
    def __init__(self):
        self.current_question = 0
        self.correct_answer = 0


quiz_state = QuizState()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🎯 Выбери уровень сложности:", reply_markup=kb.chooce_level)


@router.message(F.text == "👶Новичок")
async def send_quiz(message: types.Message):
    quiz_state.correct_answer = 0
    quiz_state.current_question = 0

    await send_next_question(message)


async def send_next_question(message: types.Message):
    question = questions[quiz_state.current_question]
    keyboard_buttons = [[types.InlineKeyboardButton(text=option, callback_data=option)]
                        for option in question['answer_options']]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    await message.answer(question['text'], reply_markup=keyboard)


@router.callback_query()
async def handler_answer(callback_query: types.CallbackQuery):
    question = questions[quiz_state.current_question]

    print(callback_query.data)
    print(question['answer_options'])

    if callback_query.data not in question['answer_options']:
        await callback_query.answer("Пожалуйста, выберите один из вариантов ответа!")
        return

    if callback_query.data == question['right_answer']:
        quiz_state.correct_answer += 1

    quiz_state.current_question += 1
    if quiz_state.current_question >= len(questions):
        await callback_query.message.answer(f"Тест завершен!\nВы правильно ответили на {quiz_state.correct_answer} вопросов.")
    else:
        await send_next_question(callback_query.message)

    await callback_query.answer()
