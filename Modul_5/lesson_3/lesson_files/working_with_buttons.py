from aiogram import Bot, Dispatcher, F, html
from aiogram.enums import ParseMode
from aiogram.types import Message, BotCommand, KeyboardButton, InlineKeyboardButton, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
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


async def button_handler():
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="Login"),
        KeyboardButton(text="Register"),
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


async def inline_button():
    inline = InlineKeyboardBuilder()
    inline.add(
        InlineKeyboardButton(text="Location", callback_data="location"),
        InlineKeyboardButton(text="Home", callback_data="home"),
        InlineKeyboardButton(text="About", callback_data="about"),
        InlineKeyboardButton(text="Contact", callback_data="contact"),
    )
    inline.adjust(2)
    return inline.as_markup()


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:

    await message.bot.set_my_commands([BotCommand(command="/start", description="Start"), BotCommand(command="/help", description="Help")])


    reply_keyboard = await button_handler()
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=reply_keyboard)


    inline_keyboard = await inline_button()
    await message.answer("Please choose an option:", reply_markup=inline_keyboard)

@dp.callback_query(lambda c: c.data in ["location", "home", "about", "contact"])
async def handle_callback_query(query: CallbackQuery) -> None:
    await query.message.edit_text(f"You selected {query.data}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
