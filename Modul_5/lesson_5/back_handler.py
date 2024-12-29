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



TOKEN = "7026470459:AAFut-PH00ZXVuG5cdPN-xQ6TBGxTE7Kq4g"


if not TOKEN:
    raise ValueError("Bot token is not found in the .env file")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


class UserStates(StatesGroup):
    books_to_main = State()
    movies_to_main = State()
    science_to_movies = State()
    science_to_books = State()
    book_to_category = State()
    movie_to_category = State()


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

@dp.message(UserStates.books_to_main, F.text == "Back")
@dp.message(UserStates.movies_to_main, F.text == "Back")
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.bot.set_my_commands([BotCommand(command="/start", description="Start"), BotCommand(command="/help", description="Help")])
    states = ["Books", "Movies"]
    adjust = [1, 1]
    inline_keyboard = make_keyboard_button(states, adjust)
    await message.answer("Please choose an option:", reply_markup=inline_keyboard)


@dp.message(F.text == "Books")
@dp.message(UserStates.science_to_books, F.text == "Back")
async def books_handler(message: Message, state: FSMContext):
    buttons = ["Science Fiction", "Drama", "Philosophy", "Romance", "Thriller", "Biography", "Back"]
    adjust = [2, 2, 2, 1]
    keyboard = make_keyboard_button(buttons, adjust)
    await state.set_state(UserStates.books_to_main)
    await message.answer("Please choose an option:", reply_markup=keyboard)


@dp.message(F.text == "Movies")
@dp.message(UserStates.science_to_movies, F.text == "Back")
async def movies_handler(message: Message, state: FSMContext):
    buttons = ["Science Fiction", "Drama", "Action", "Romance", "Thriller", "Fantasy", "Back"]
    adjust = [2, 2, 2, 1]
    keyboard = make_keyboard_button(buttons, adjust)
    await state.set_state(UserStates.movies_to_main)
    await message.answer("Please choose an option:", reply_markup=keyboard)




@dp.message(UserStates.book_to_category, F.text == "Back")
@dp.message(UserStates.books_to_main, F.text == "Science Fiction")
async def books_science_fiction_handler(message: Message, state: FSMContext):
    buttons = ["Dune", "Foundation", "Neuromancer", "Snow Crash", "Back"]
    adjust = [2, 2, 1]
    keyboard = make_keyboard_button(buttons, adjust)
    await state.set_state(UserStates.science_to_books)
    await message.answer("Please choose a Science Fiction book:", reply_markup=keyboard)

@dp.message(UserStates.movie_to_category, F.text == "Back")
@dp.message(UserStates.movies_to_main, F.text == "Science Fiction")
async def movies_science_fiction_handler(message: Message, state: FSMContext):
    buttons = ["Back to the Future", "Interstellar", "Inception", "The Matrix", "Back"]
    adjust = [2, 2, 1]
    keyboard = make_keyboard_button(buttons, adjust)
    await state.set_state(UserStates.science_to_movies)
    await message.answer("Please choose a Science Fiction movie:", reply_markup=keyboard)




@dp.message(UserStates.science_to_books, F.text == "Dune")
async def books_science_fiction_handler(message: Message, state: FSMContext):
    buttons = ["Dune 1", "Dune 2", "Dune 3", "Dune 4", "Dune 5", "Back"]
    adjust = [2, 2, 1, 1]
    keyboard = make_keyboard_button(buttons, adjust)
    await state.set_state(UserStates.book_to_category)
    await message.answer("Please choose a Science Fiction book:", reply_markup=keyboard)

@dp.message(UserStates.science_to_movies, F.text == "Back to the Future")
async def movies_science_fiction_handler(message: Message, state: FSMContext):
    buttons = ["Back to the Future", "Back to the Future 2", "Back to the Future 3",  "Back"]
    adjust = [2, 1, 1]
    keyboard = make_keyboard_button(buttons, adjust)
    await state.set_state(UserStates.movie_to_category)
    await message.answer("Please choose a Science Fiction movie:", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


