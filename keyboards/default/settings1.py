from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

settings1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="P/4/1/I-ENS"),
            KeyboardButton(text="P/3/1/I-ENS"),
            KeyboardButton(text="P/2/1/I-ENS"),
            KeyboardButton(text="P/1/1/I-ENS"),
        ],
        [
            KeyboardButton(text="P/4/2/I-ENS"),
            KeyboardButton(text="P/3/2/I-ENS"),
            KeyboardButton(text="P/2/2/I-ENS"),
            KeyboardButton(text="P/1/2/I-ENS"),

        ],
        [
            KeyboardButton(text="P/4/3/I-ENS"),
            KeyboardButton(text="P/3/3/I-ENS"),
            KeyboardButton(text="P/2/3/I-ENS"),
            KeyboardButton(text="P/1/3/I-ENS"),
        ],
        [
            KeyboardButton(text="Go back to Menu")
        ],
    ],
    resize_keyboard=True
)