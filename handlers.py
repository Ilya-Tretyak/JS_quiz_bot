from aiogram import types, Router, F
from aiogram.filters.command import Command
import kb
from questions import questions

router = Router()


class QuizState:
    def __init__(self):
        self.current_question = 0
        self.correct_answer = 0
        self.message_id = None  # Добавляем хранение id сообщения с вопросом


quiz_state = QuizState()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🎯 Выбери уровень сложности:", reply_markup=kb.choose_level)


@router.message(F.text == "👶Новичок")
async def send_quiz(message: types.Message):
    quiz_state.current_question = 0
    quiz_state.correct_answer = 0
    quiz_state.message_id = None  # Сбрасываем id сообщения

    await send_next_question(message)


async def send_next_question(message: types.Message):
    question = questions[quiz_state.current_question]
    keyboard_buttons = [types.InlineKeyboardButton(text=option, callback_data=option)
                        for option in question['answer_options']]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[keyboard_buttons])

    if quiz_state.message_id:
        await message.bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=quiz_state.message_id,
            text=question['text'],
            reply_markup=keyboard
        )
    else:
        sent_message = await message.answer(question['text'], reply_markup=keyboard)
        quiz_state.message_id = sent_message.message_id  # Сохраняем id отправленного сообщения


@router.callback_query()
async def handle_answer(callback_query: types.CallbackQuery):
    question = questions[quiz_state.current_question]

    if callback_query.data not in question['answer_options']:
        await callback_query.answer("Пожалуйста, выберите один из предложенных вариантов ответа.")
        return

    if callback_query.data == question['right_answer']:
        quiz_state.correct_answer += 1

    quiz_state.current_question += 1
    if quiz_state.current_question >= len(questions):
        await callback_query.message.answer(
            f"Тест завершен!\nВы правильно ответили на {quiz_state.correct_answer} вопросов."
        )
        if quiz_state.message_id:
            await callback_query.message.bot.delete_message(
                    chat_id=callback_query.message.chat.id,
                    message_id=quiz_state.message_id
                )
    else:
        await send_next_question(callback_query.message)

    await callback_query.answer()
