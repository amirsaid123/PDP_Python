from os import getenv
from aiogram.types import  InlineKeyboardButton
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import  InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from aiogram.client.default import DefaultBotProperties
import asyncio
import logging
import sys
from flask.cli import load_dotenv

load_dotenv(r"D:\PDP Python\Modul_5\lesson_4_homework\.env")
TOKEN = getenv("TOKEN")



if not TOKEN:
    raise ValueError("Bot token is not found in the .env file")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()




command_usage = {"start": 0, "help": 0}

@dp.message(CommandStart())
async def start_handler(message: Message):
    command_usage["start"] += 1

    inline_keyboard = InlineKeyboardBuilder()
    inline_keyboard.add(InlineKeyboardButton(text="Statistics", callback_data="statistics"))


    await message.answer("You pressed the /start command!")
    await message.answer("Please choose an option:", reply_markup=inline_keyboard.as_markup())

@dp.message(Command("help"))
async def help_handler(message: Message):
    command_usage["help"] += 1
    await message.answer("You pressed the /help command!")

@dp.callback_query(F.data == "statistics")
async def statistics_handler(callback: CallbackQuery):

    start_count = command_usage["start"]
    help_count = command_usage["help"]
    await callback.message.answer(f"You pressed /start {start_count} times and /help {help_count} times.")


    await callback.message.edit_reply_markup(reply_markup=None)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())