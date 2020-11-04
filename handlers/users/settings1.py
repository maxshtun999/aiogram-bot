from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import start, settings1
from loader import dp
import psycopg2


@dp.message_handler(Command("Settings"))
async def show_settings(message: Message):
    await message.answer("Settings", reply_markup=settings1)


@dp.message_handler(content_types=["text"])
async def handle_text(message):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1Z2z3z4z",
                                      host="localhost",
                                      port="5432",
                                      database="Wsei")
        connection.autocommit = True
        userid = message.from_user.id
        text = message.text
        cur = connection.cursor()
        if text == '':
            print("error empty line")
        else:
            print(text, userid)
            cur.execute("""Insert into public."Users" (group_name)  values (%s) """,[text])

            print(text, userid)
            count = cur.rowcount
            print(count, "Record inserted successfully into table")
        connection.commit()


    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into table", error)


    finally:
        if (connection):
            connection.close()
            print("PostgreSQL connection is closed")
    await message.answer(f"Your group name is {text}",
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(
    equals=["Change Group name (Send me group name and press this button)"]))
async def set_group_name(message: types.Message):
    await message.answer("Go back to Menu", reply_markup=start)


@dp.message_handler(Text(equals=["Go back to Menu"]))
async def get_back(message: Message):
    await message.answer("Go back to Menu", reply_markup=start)
