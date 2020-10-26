from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import start, settings1
from loader import dp


@dp.message_handler(Command("Start"))
async def show_menu(message: Message):
    await message.answer("Hello welcome to WSEi schedule bot. Please choose "
                         "option.", reply_markup=start)


@dp.message_handler(Text(equals=["Search Group Schedule"]))
async def get_schedule(message: Message):
    await message.answer(f"You choose111 {message.text}. Thanks",
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["Settings"]))
async def get_settings(message: Message):
    await message.answer("Settings",
                         reply_markup=settings1)


@dp.message_handler(Text(equals=["Help"]))
async def get_help(message: Message):
    await message.answer(f"If you faced with bug or problem during using "
                         f"this bot please contact with @pUGShOLE, "
                         f"or try to find sollution in frequent asked questions"
                         "\n""frequent asked questions:"
                         "\n""1)I can not see my schedule why? "
                         "\n""It can be caused by typo in Group name, please "
                         "check correctness in Setting menu ( /settings )."
                         "\n""2)Any other problem?"
                         "\n""contact with @pUGShOLE",
                         reply_markup=ReplyKeyboardRemove())
