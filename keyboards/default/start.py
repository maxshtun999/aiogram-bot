from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Search Group Schedule"),
        ],
        [
            KeyboardButton(text="Help"),
            KeyboardButton(text="Settings")
        ],
    ],
    resize_keyboard=True
)