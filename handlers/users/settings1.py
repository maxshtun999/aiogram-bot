from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import start, settings1
from loader import dp
import psycopg2


@dp.message_handler(Command("Settings"))
async def show_settings(message: Message):
    await message.answer("Settings", reply_markup=settings1)


@dp.message_handler(Text(equals=["Change Group name (Send me group name and press this button)"]))
async def set_group_name(message: Message):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1Z2z3z4z",
                                      host="localhost",
                                      port="5432",
                                      database="Wsei_schedule")



        cursor = connection.cursor()
        userid = message.from_user.id
        cur = connection.cursor()
        cur.execute(
            """SELECT tg_id FROM public."Users" WHERE (tg_id) = (%s) """,
            [userid])
        cur.execute("""INSERT INTO public."Users" (tg_id) VALUES (%s)""",
                    [userid])

        connection.commit()



        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO "User".users(group) VALUES (%s)"""
        record_to_insert = (5)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into table")

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into table", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    await message.answer("Change Group name",
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["Go back to Menu"]))
async def get_back(message: Message):
    await message.answer("Go back to Menu", reply_markup=start)

