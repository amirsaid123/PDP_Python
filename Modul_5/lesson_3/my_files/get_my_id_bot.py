from aiogram import Bot, Dispatcher, F, html
from aiogram.enums import ParseMode
from aiogram.types import Message, BotCommand, KeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from os import getenv
from dotenv import load_dotenv
from aiogram.client.default import DefaultBotProperties
import asyncio
import logging
import sys

load_dotenv(r"/Modul_5/.env")
TOKEN = getenv("TUKUN")

if not TOKEN:
    raise ValueError("Bot token is not found in the .env file")


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def button_handler():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="My ID"))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.bot.set_my_commands([BotCommand(command="/start", description="Start"),
                                       BotCommand(command="/help", description="Help")])
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message(Command("help"))
async def help_handler(message: Message):
    keyboard = await button_handler()
    await message.answer("Click My ID to get your ID", reply_markup=keyboard)

@dp.message(F.text == "My ID")
async def send_user_id(message: Message):
    user_id = message.from_user.id
    await message.answer(f"Your Telegram ID is: <code>{user_id}</code>")

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
