from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

settings1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Change Group name"),
        ],
        [
            KeyboardButton(text="Go back to Menu")
        ],
    ],
    resize_keyboard=True
)