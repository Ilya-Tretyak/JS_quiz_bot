from aiogram import types, Router, F
from aiogram.filters.command import Command
import kb
from questions import questions_for_beginner

router = Router()


class QuizState:
    def __init__(self):
        self.current_question = 0
        self.correct_answer = 0
        self.message_id = None  # Добавляем хранение id сообщения с вопросом


user_states = {}


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    user_states[user_id] = QuizState()
    await message.answer("🎯 Выбери уровень сложности:", reply_markup=kb.choose_level)


@router.message(F.text == "👶Новичок")
async def send_quiz(message: types.Message):
    user_id = message.from_user.id
    quiz_state = user_states.get(user_id)

    if quiz_state:
        quiz_state.current_question = 0
        quiz_state.correct_answer = 0
        quiz_state.message_id = None  # Сбрасываем id сообщения

    await send_next_question(message, user_id)


async def send_next_question(message: types.Message, user_id: int):
    quiz_state = user_states.get(user_id)
    if not quiz_state:
        return

    question = questions_for_beginner[quiz_state.current_question]
    keyboard_buttons = [[types.InlineKeyboardButton(text=option, callback_data=option)]
                        for option in question['answer_options']]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

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
    user_id = callback_query.from_user.id
    quiz_state = user_states.get(user_id)
    if not quiz_state:
        return

    question = questions_for_beginner[quiz_state.current_question]

    if callback_query.data not in question['answer_options']:
        await callback_query.answer("Пожалуйста, выберите один из предложенных вариантов ответа.")
        return

    if callback_query.data == question['right_answer']:
        quiz_state.correct_answer += 1

    quiz_state.current_question += 1
    if quiz_state.current_question >= len(questions_for_beginner):
        await callback_query.message.answer(
            f"Тест завершен!\nВы правильно ответили на {quiz_state.correct_answer} вопросов."
        )
        user_states.pop(user_id, None)

        if quiz_state.message_id:
            await callback_query.message.bot.delete_message(
                    chat_id=callback_query.message.chat.id,
                    message_id=quiz_state.message_id
                )
    else:
        await send_next_question(callback_query.message, user_id)

    await callback_query.answer()
