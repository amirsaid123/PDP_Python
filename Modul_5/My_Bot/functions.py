import json
from aiogram import Bot, Dispatcher, F, html
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand, KeyboardButton, InputFile
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup
from os import getenv
from dotenv import load_dotenv
from aiogram.client.default import DefaultBotProperties
import asyncio
import logging
import sys
from aiogram.fsm.state import State, StatesGroup

load_dotenv(r"D:\PDP Python\Modul_5\.env")
TOKEN = getenv("TIKIN")

if not TOKEN:
    raise ValueError("Bot token is not found in the .env file")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


class CommentState(StatesGroup):
    waiting_for_comment = State()
    waiting_for_area = State()
    waiting_for_city_area = State()
    waiting_for_region_area = State()
    waiting_for_job = State()


tashkent_city_areas = ["Uchtepa", "Sergeli", "Yakkasaroy", "Mirzoulug`bek", "Shayxontoxur", "Chilonzor",
                       "Olmazor", "Yangi Hayot", "Mirobod", "Yunusobod", "Yashnabod", "Bektemir"]

tashkent_region_areas = ["Yangiyo`l", "Toshkent", "Bo`stonliq", "Chinoz", "Zangiota", "Yuqorichirchiq"]


async def cities_keyboard():
    back_button = KeyboardButton(text="Back")
    city1 = KeyboardButton(text="Tashkent City")
    city2 = KeyboardButton(text="Tashkent Region")
    builder = ReplyKeyboardBuilder()
    builder.add(city1, city2, back_button)
    builder.adjust(2, 2, 2)
    return builder.as_markup(resize_keyboard=True)

async def cities_menu():
    city1 = KeyboardButton(text=tashkent_city_areas[0])
    city2 = KeyboardButton(text=tashkent_city_areas[1])
    city3 = KeyboardButton(text=tashkent_city_areas[2])
    city4 = KeyboardButton(text=tashkent_city_areas[3])
    city5 = KeyboardButton(text=tashkent_city_areas[4])
    city6 = KeyboardButton(text=tashkent_city_areas[5])
    city7 = KeyboardButton(text=tashkent_city_areas[6])
    city8 = KeyboardButton(text=tashkent_city_areas[7])
    city9 = KeyboardButton(text=tashkent_city_areas[8])
    city10 = KeyboardButton(text=tashkent_city_areas[9])
    city11 = KeyboardButton(text=tashkent_city_areas[10])
    city12 = KeyboardButton(text=tashkent_city_areas[11])
    back_button = KeyboardButton(text="Back")
    main_menu = KeyboardButton(text="Main Menu")
    builder = ReplyKeyboardBuilder()
    builder.add(city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, back_button,
                main_menu)
    builder.adjust(2, 2, 2)
    return builder.as_markup(resize_keyboard=True)

async def regions_menu():
    region1 = KeyboardButton(text=tashkent_region_areas[0])
    region2 = KeyboardButton(text=tashkent_region_areas[1])
    region3 = KeyboardButton(text=tashkent_region_areas[2])
    region4 = KeyboardButton(text=tashkent_region_areas[3])
    region5 = KeyboardButton(text=tashkent_region_areas[4])
    region6 = KeyboardButton(text=tashkent_region_areas[5])
    back_button = KeyboardButton(text="Back")
    main_menu = KeyboardButton(text="Main Menu")
    builder = ReplyKeyboardBuilder()
    builder.add(region1, region2, region3, region4, region5, region6, back_button, main_menu)
    builder.adjust(2, 2, 2)
    return builder.as_markup(resize_keyboard=True)

async def jobs_menu():
    back_button = KeyboardButton(text="Back")
    main_menu = KeyboardButton(text="Main Menu")
    job1 = KeyboardButton(text="Cook")
    job2 = KeyboardButton(text="Dish Washer")
    job3 = KeyboardButton(text="Cleaner")
    job4 = KeyboardButton(text="Table cleaner")
    job5 = KeyboardButton(text="Barman")
    job6 = KeyboardButton(text="Courier")
    builder = ReplyKeyboardBuilder()
    builder.add(job1, job2, job3, job4, job5, job6, back_button, main_menu)
    builder.adjust(2, 2, 2)
    return builder.as_markup(resize_keyboard=True)

async def main_menu():
    button1 = KeyboardButton(text="About Our Company 🏢")
    button2 = KeyboardButton(text="Vacancies 💼")
    button3 = KeyboardButton(text="Menu 🍟")
    button4 = KeyboardButton(text="Comments and offers 💬")
    button5 = KeyboardButton(text="Contacts and Address 📞")
    button6 = KeyboardButton(text="Language uzb/eng/rus")
    builder = ReplyKeyboardBuilder()
    builder.add(
        button1,
        button2,
        button3,
        button4,
        button5,
        button6,
    )
    builder.adjust(2, 2, 2)
    return builder.as_markup(resize_keyboard=True)

async def save_comment(user_info, comment):
    with open("D:\PDP Python\Modul_5\My_Bot\comments.json", "r", encoding="utf-8") as f:
        comments_data = json.load(f)

    comments_data.append({
        "user_id": user_info.id,
        "username": user_info.username,
        "full_name": user_info.full_name,
        "comment": comment
    })
    with open("comments.json", "w", encoding="utf-8") as file:
        json.dump(comments_data, file, ensure_ascii=False, indent=4)

