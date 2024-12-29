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

actions = [
    {"action": "like", "id": 1},
    {"action": "dislike", "id": 2},
    {"action": "comment", "id": 3},
    {"action": "share", "id": 4},
    {"action": "follow", "id": 5},
    {"action": "unfollow", "id": 6},
    {"action": "subscribe", "id": 7},
    {"action": "unsubscribe", "id": 8},
    {"action": "report", "id": 9},
    {"action": "save", "id": 10},
]




def make_keyboard_button(btns_name : list , adjust: list):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[KeyboardButton(text = name) for name in btns_name])
    rkb.adjust(*adjust)
    return rkb.as_markup(resize_keyboard=True)

def make_inline_button(btns_name : list , adjust: list):
    inline = InlineKeyboardBuilder()
    inline.add(*[InlineKeyboardButton(text = action['action'].capitalize(), callback_data=f"{action['action']}:{action['id']}") for action in btns_name])
    inline.adjust(*adjust)
    return inline.as_markup()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.bot.set_my_commands([BotCommand(command="/start", description="Start"), BotCommand(command="/help", description="Help")])
    adjust = [2, 2]
    inline_keyboard = make_inline_button(actions, adjust)
    await message.answer("Please choose an option:", reply_markup=inline_keyboard)

@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    action_name, action_id = callback.data.split(":")
    if int(action_id) % 2 == 0:
        await callback.answer()
        await callback.message.answer(f"You pressed {action_name}")
    else:
        await callback.answer()
        await callback.message.answer(f"Get out of here")





async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


