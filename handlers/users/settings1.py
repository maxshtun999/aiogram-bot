from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from keyboards.default import start, settings1
from loader import dp
import psycopg2


@dp.message_handler(Command("Settings"))
async def show_settings(message: Message):
    await message.answer("Settings", reply_markup=settings1)


@dp.message_handler(Text(
    equals=["P/4/1/I-ENS", "P/4/2/I-ENS", "P/4/3/I-ENS", "P/3/1/I-ENS",
            "P/3/2/I-ENS", "P/3/3/I-ENS", "P/2/1/I-ENS", "P/2/2/I-ENS",
            "P/2/3/I-ENS", "P/1/1/I-ENS", "P/1/2/I-ENS", "P/1/3/I-ENS"]))
async def set_group_name(message: types.Message):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1Z2z3z4z",
                                      host="localhost",
                                      port="5432",
                                      database="Wsei")
        connection.autocommit = True
        user_id = message.from_user.id
        text = message.text
        cur = connection.cursor()
        cur.execute("""DELETE FROM public."Users" WHERE tg_id = (%s)""",
                    [user_id])
        print("deleted")
        if text == "":
            print("error empty line")
        else:
            data = [(user_id, text)]
            records_list_template = ','.join(['%s'] * len(data))
            insert_query = """Insert into public."Users" (tg_id, group_name)  values {}""".format(
                records_list_template)
            cur.execute(insert_query, data)
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
    await message.answer(f"Your group name is {text}", reply_markup=start)


@dp.message_handler(Text(equals=["Go back to Menu"]))
async def get_back(message: Message):
    await message.answer("Go back to Menu", reply_markup=start)
