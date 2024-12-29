import json
from os import getenv

from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, KeyboardButton, InlineKeyboardButton, CallbackQuery, BotCommand
from aiogram import Bot, Dispatcher, F, html
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from flask.cli import load_dotenv
import asyncio
import logging
import sys

load_dotenv(r"D:\PDP Python\Modul_5\lesson_4_homework\.env")
TOKEN = getenv("TOKEN")

if not TOKEN:
    raise ValueError("Bot token is not found in the .env file")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


class UserStates(StatesGroup):
    first_question = State()
    second_question = State()
    third_question = State()


def make_keyboard_button(btns_name : list , adjust: list):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[KeyboardButton(text = name) for name in btns_name])
    rkb.adjust(*adjust)
    return rkb.as_markup(resize_keyboard=True)


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.bot.set_my_commands([BotCommand(command="/start", description="Start")])
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}")
    inline_keyboard = make_keyboard_button(["Questions"], adjust=[1])
    await message.answer("Please choose an option:", reply_markup=inline_keyboard)

@dp.message(F.text == "Questions")
async def savollar_handler(message: Message, state: FSMContext):
    await state.set_state(UserStates.first_question)
    await message.answer("1 + 1 equals?")

@dp.message(UserStates.first_question)
async def first_question_handler(message: Message, state: FSMContext):
    if message.text == "2":
        await message.answer("Correct!")
        await state.set_state(UserStates.second_question)
        await message.answer("Does the Earth revolve around the Sun? (yes/no)")
    else:
        await message.answer("Incorrect. Try again!")
        await message.answer("1 + 1 equals?")

@dp.message(UserStates.second_question)
async def second_question_handler(message: Message, state: FSMContext):
    if message.text.lower() == "yes":
        await message.answer("Correct!")
        await state.set_state(UserStates.third_question)
        await message.answer("Do millions of developers use Python annually? (yes/no)")
    else:
        await message.answer("Incorrect. Try again!")
        await message.answer("Does the Earth revolve around the Sun? (yes/no)")

@dp.message(UserStates.third_question)
async def third_question_handler(message: Message, state: FSMContext):
    if message.text.lower() == "yes":
        await message.answer("Congratulations! You answered all questions correctly!")
        await state.clear()
    else:
        await message.answer("Incorrect. Try again!")
        await message.answer("Do millions of developers use Python annually? (yes/no)")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
