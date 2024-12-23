from aiogram import Bot, Dispatcher, F, html
from aiogram.enums import ParseMode
from aiogram.types import Message, BotCommand
from aiogram.filters import CommandStart
from os import getenv
from dotenv import load_dotenv
from aiogram.client.default import DefaultBotProperties
import asyncio
import logging
import sys

load_dotenv(r"/Modul_5/.env")
TOKEN = getenv("TOKEN")

if not TOKEN:
    raise ValueError("Bot token is not found in the .env file")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message:Message) -> None:
    await message.bot.set_my_commands([BotCommand(command="/start" , description="Start"), BotCommand(command="/help", description="Help")])
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo(message: Message):
    text = message.text
    text = text[::-1]
    await message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())






































