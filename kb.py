from aiogram. types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


chooce_level_button = [
        [KeyboardButton(text="👶Новичок", callback_data="beginner")],
        [KeyboardButton(text="🚀Продвинутый", callback_data="advanced")],
        [KeyboardButton(text="🔥Эксперт", callback_data="expert")]
]
"""Reply клавиатура, выбор уровня сложности"""
chooce_level = ReplyKeyboardMarkup(keyboard=chooce_level_button, resize_keyboard=True)
