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

load_dotenv(r"D:\PDP Python\Modul_5\lesson_4_homework\.env")
TOKEN = getenv("TOKEN")



if not TOKEN:
    raise ValueError("Bot token is not found in the .env file")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


class UserStates(StatesGroup):
    first = State()
    second = State()
    third = State()
    last = State()

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


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.bot.set_my_commands([BotCommand(command="/start", description="Start"), BotCommand(command="/help", description="Help")])
    states = ["First", "Second", "Third", "Last"]
    adjust = [2, 2]
    inline_keyboard = make_inline_button(states, adjust)
    await message.answer("Please choose an option:", reply_markup=inline_keyboard)

user_data = {}

@dp.callback_query(F.data == "first")
async def handle_first(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(UserStates.first)
    user_id = callback.from_user.id
    user_data.setdefault(user_id, []).append("First State")
    await callback.message.answer("This is the First State. Please choose the next button.")


@dp.callback_query(F.data == "second")
async def handle_second(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(UserStates.second)
    user_id = callback.from_user.id
    user_data.setdefault(user_id, []).append("Second State")
    await callback.message.answer("This is the Second State. Please choose the next button.")

@dp.callback_query(F.data == "third")
async def handle_second(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(UserStates.second)
    user_id = callback.from_user.id
    user_data.setdefault(user_id, []).append("Third State")
    await callback.message.answer("This is the Third State. Please choose the next button.")


@dp.callback_query(F.data == "last")
async def handle_last(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(UserStates.last)
    await callback.message.delete()
    user_id = callback.from_user.id
    user_data.setdefault(user_id, []).append("Final State")
    summary = "\n".join(user_data.get(user_id, []))
    await callback.message.answer(f"Process completed. Selected states:\n{summary}")



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


