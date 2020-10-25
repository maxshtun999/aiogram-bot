from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import start, settings1
from loader import dp


@dp.message_handler(Command("Settings"))
async def show_settings(message: Message):
    await message.answer("Settings", reply_markup=settings1)


@dp.message_handler(Text(equals=["Change Group name"]))
async def get_food(message: Message):
    await message.answer("Change Group name", reply_markup=ReplyKeyboardRemove())



@dp.message_handler(Text(equals=["Go back to Menu"]))
async def get_food(message: Message):
    await message.answer("Go back to Menu", reply_markup=start)
    #show_menu(message)
    #eply_markup=ReplyKeyboardRemove())