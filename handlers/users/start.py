from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import start, settings1
from loader import dp
import psycopg2


@dp.message_handler(Command("Start"))
async def show_menu(message: types.Message):
    await message.answer("Hello welcome to WSEi schedule bot. Please choose "
                         "option.", reply_markup=start)


@dp.message_handler(Text(equals=["Search Group Schedule"]))
async def get_schedule(message: Message):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1Z2z3z4z",
                                      host="localhost",
                                      port="5432",
                                      database="Wsei")
        connection.autocommit = True
        user_id = message.from_user.id
        cur = connection.cursor()
        if user_id == "":
            print("error empty line")
        else:
            cur.execute("""SELECT date11, time_from, time_to, lesson, room, lecturer_name, group_name  from schedule, "Users" where group_name = group1 ORDER BY date11""")
            data = cur.fetchall()
            data1 = '\n'.join(map(str, data))
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into table", error)

    finally:
        if (connection):
            connection.close()
            print("PostgreSQL connection is closed")
    if not data:
        await message.answer(
            f"Please go to Settings (/settings) and choose group!",
            reply_markup=ReplyKeyboardRemove())

    else:
        await message.answer(f"{data1}",
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
