from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

settings1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Change Group name (Send me group name and press this button)"),
        ],
        [
            KeyboardButton(text="Go back to Menu")
        ],
    ],
    resize_keyboard=True
)