from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandSettings
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'Settings')
@dp.message_handler(CommandSettings())
async def bot_Settings(message: types.Message):
    text = [
        f"If you faced with bug or problem during using "
        f"this bot please contact with @pUGShOLE, "
        f"or try to find sollution in frequent asked questions"
        "\n""frequent asked questions:"
        "\n""1)I can not see my schedule why? "
        "\n""It can be caused by typo in Group name, please "
        "check correctness in Setting menu ( /settings )."
        "\n""2)Any other problem?"
        "\n""contact with @pUGShOLE"
    ]
    await message.answer('\n'.join(text))
