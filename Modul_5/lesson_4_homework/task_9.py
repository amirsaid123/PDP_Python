import json
from os import getenv
from random import setstate
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, CallbackQuery
from aiogram import Bot, Dispatcher, F, html
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand, KeyboardButton, InputFile, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import CallbackQuery
from aiogram.client.default import DefaultBotProperties
import asyncio
import logging
import sys
from aiogram.fsm.state import State, StatesGroup
from flask.cli import load_dotenv
from mimetypes import guess_type
load_dotenv(r"D:\PDP Python\Modul_5\lesson_4_homework\.env")
TOKEN = getenv("TOKEN")



if not TOKEN:
    raise ValueError("Bot token is not found in the .env file")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


class UserStates(StatesGroup):
    waiting_files = State()
    waiting_fullname = State()
    waiting_contact = State()
    sending_files = State()
def make_keyboard_button(btns_name : list , adjust: list):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[KeyboardButton(text = name) for name in btns_name])
    rkb.adjust(*adjust)
    return rkb.as_markup(resize_keyboard=True)

def make_inline_button(btns_name : list , adjust: list):
    inline = InlineKeyboardBuilder()
    inline.add(*[InlineKeyboardButton(text = name, callback_data=name.lower()) for name in btns_name])
    inline.adjust(*adjust)
    return inline.as_markup()

def make_contact_button():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Share Contact", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await message.bot.set_my_commands([BotCommand(command="/start", description="Start"), BotCommand(command="/help", description="Help")])
    states = ["Send Files"]
    adjust = [1]
    keyboard = make_keyboard_button(states, adjust)
    await state.set_state(UserStates.waiting_files)
    await message.answer("Please choose an option:", reply_markup=keyboard)

user_data = {}
@dp.message(UserStates.waiting_files)
async def file_handler(message: Message, state: FSMContext):
    if not message.document:
        await state.set_state(UserStates.waiting_files)
        await message.answer("Please send a valid file:", reply_markup=None)
    else:
        file = message.document
        file_name = file.file_name
        file_id = file.file_id
        mime_type, _ = guess_type(file_name)

        if mime_type and mime_type.startswith("image"):
            user_data[message.from_user.id] = {
                "file_name": file_name,
                "file_id": file_id,
                "user_id": message.from_user.id,
            }
        else:
            pass

        await state.set_state(UserStates.waiting_fullname)
        await message.asnwer("Please, enter your fullname")

@dp.message(UserStates.waiting_fullname)
async def fullname_handler(message: Message, state: FSMContext):
    user_data["user_id"]["fullname"] = message.text
    await state.set_state(UserStates.waiting_contact)
    await message.answer("Please share your contact:", reply_markup=make_contact_button())


@dp.message(UserStates.waiting_contact)
async def contact_handler(message: Message, state: FSMContext):
    if not message.contact:
        await message.reply(
            "Please use the 'Share Contact' button to share your contact info.",
            reply_markup=make_contact_button(),
        )
        return

    contact = message.contact.phone_number
    user_id = message.from_user.id

    if user_id in user_data:
        user_data[user_id]["contact"] = contact

        formatted_data = "\n".join(
            [
                f"{key.capitalize()}: {value}"
                for key, value in user_data[user_id].items()
                if key != "file_id"
            ]
        )
        file_id = user_data[user_id]["file_id"]
        await bot.send_document(
            chat_id=user_id,
            document=file_id,
            caption=f"Here is your submitted data:\n\n{formatted_data}",
        )

        await message.reply("Thank you! All your data has been sent back to you.")
        await state.clear()
    else:
        await message.reply("No file information found. Please start over by sending a file.")

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


