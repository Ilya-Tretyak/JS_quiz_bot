from aiogram import types, Router, F
from aiogram.filters.command import Command

from questions import (
    questions_for_beginner,
    questions_for_advanced,
    questions_for_expert
)

router = Router()


class QuizState:
    def __init__(self):
        self.current_question = 0
        self.correct_answer = 0
        self.message_id = None  # Добавляем хранение id сообщения с вопросом
        self.questions_lvl = str()  # Добавляем хранение уровня сложности
        self.questions = list()


user_states = {}


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    quiz_state = user_states.get(user_id)

    if quiz_state:
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        user_states.pop(user_id, None)

    user_states[user_id] = QuizState()

    choose_level = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="👶Новичок", callback_data="beginner")],
            [types.InlineKeyboardButton(text="🚀Продвинутый", callback_data="advanced")],
            [types.InlineKeyboardButton(text="🔥Эксперт", callback_data="expert")]
        ]
    )

    sent_message = await message.answer("🎯 Выбери уровень сложности:", reply_markup=choose_level)
    user_states[user_id].message_id = sent_message.message_id

    await message.delete()


@router.callback_query(F.data == "beginner")
@router.callback_query(F.data == "advanced")
@router.callback_query(F.data == "expert")
async def send_quiz(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    quiz_state = user_states.get(user_id)

    if quiz_state:
        quiz_state.current_question = 0
        quiz_state.correct_answer = 0
        quiz_state.questions_lvl = callback_query.data
        quiz_state.questions = list()

    await send_next_question(callback_query.message, user_id)


async def send_next_question(message: types.Message, user_id: int):
    quiz_state = user_states.get(user_id)

    if not quiz_state:
        return

    if quiz_state.questions_lvl == "beginner":
        questions = questions_for_beginner
    elif quiz_state.questions_lvl == "advanced":
        questions = questions_for_advanced
    else:
        questions = questions_for_expert

    quiz_state.questions = questions
    question = quiz_state.questions[quiz_state.current_question]

    keyboard_buttons = [[types.InlineKeyboardButton(text=option, callback_data=str(index))]
                        for index, option in enumerate(question['answer_options'])]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    await message.bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=quiz_state.message_id,
            text=f"{question['text']}",
            reply_markup=keyboard
        )


@router.callback_query()
async def handle_answer(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    quiz_state = user_states.get(user_id)
    if not quiz_state:
        return

    question = quiz_state.questions[quiz_state.current_question]
    print(callback_query.data)

    if not question['answer_options'][int(callback_query.data)]:
        await callback_query.answer("Пожалуйста, выберите один из предложенных вариантов ответа.")
        return

    if question['answer_options'][int(callback_query.data)] == question['right_answer']:
        quiz_state.correct_answer += 1

    quiz_state.current_question += 1
    if quiz_state.current_question >= len(quiz_state.questions):
        await callback_query.message.answer(
            f"Тест завершен!\nВы правильно ответили на"
            f" {quiz_state.correct_answer} из {len(quiz_state.questions)} вопросов."
        )

        if quiz_state.message_id:
            await callback_query.message.bot.delete_message(
                    chat_id=callback_query.message.chat.id,
                    message_id=quiz_state.message_id
                )
    else:
        await send_next_question(callback_query.message, user_id)

    await callback_query.answer()
