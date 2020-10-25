from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types


@dp.message_handler(Command("id"))
async def user_id(message: types.Message):
    await message.answer(f"{message.from_user.id}")
