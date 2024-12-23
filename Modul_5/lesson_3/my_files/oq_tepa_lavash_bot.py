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

load_dotenv(r"/Modul_5/.env")
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
    with open("comments.json", "r", encoding="utf-8") as f:
        comments_data = json.load(f)

    comments_data.append({
        "user_id": user_info.id,
        "username": user_info.username,
        "full_name": user_info.full_name,
        "comment": comment
    })
    with open("comments.json", "w", encoding="utf-8") as file:
        json.dump(comments_data, file, ensure_ascii=False, indent=4)


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.bot.set_my_commands([BotCommand(command="/start", description="Start"),
                                       BotCommand(command="/help", description="Help")])
    button = await main_menu()
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=button)

    photo_path = "https://imgur.com/a/quDcoY3"
    await message.answer_photo(photo_path, caption="Welcome to the best fast food in the world! 🍔🍟")


@dp.message(F.text == "About Our Company 🏢")
async def send_user_id(message: Message):
    text = """
    Amirsaid Lavash is a fast-food company dedicated to serving delicious, 
    high-quality lavash wraps that bring together fresh ingredients and bold 
    flavors. Our menu offers a variety of options, from classic recipes to 
    innovative twists, ensuring there's something for everyone.

    We prioritize fast service without compromising on taste, making us the 
    perfect spot for a quick and satisfying meal. At Amirsaid Lavash, we’re 
    passionate about creating an enjoyable dining experience, whether you're 
    grabbing lunch on the go or enjoying a cozy meal with friends.

    Taste the difference with every bite!
    """

    photo_path = "https://imgur.com/a/quDcoY3"
    await message.answer_photo(photo_path, caption=text)


@dp.message(F.text == "Vacancies 💼")
async def send_vacancies(message: Message, state: FSMContext):
    back_button = KeyboardButton(text="Back")
    tashkent_city = KeyboardButton(text="Tashkent City")
    tashkent_region = KeyboardButton(text="Tashkent Region")
    keyboard = ReplyKeyboardMarkup(keyboard=[[tashkent_city], [tashkent_region], [back_button]], resize_keyboard=True)
    await message.answer("Please choose area!", reply_markup=keyboard)
    await state.set_state(CommentState.waiting_for_area)


@dp.message(CommentState.waiting_for_area)
async def receive_area(message: Message, state: FSMContext):
    if message.text == "Back":
        await state.clear()
        menu = await main_menu()
        await message.answer("Returning to the main menu...", reply_markup=menu)

    elif message.text == "Tashkent City":
        city_keyboard = await cities_menu()
        await message.answer("Please choose area in the Tashkent City!", reply_markup=city_keyboard)
        await state.set_state(CommentState.waiting_for_city_area)

    elif message.text == "Tashkent Region":
        region_keyboard = await regions_menu()
        await message.answer("Please choose area in the Tashkent Region!", reply_markup=region_keyboard)
        await state.set_state(CommentState.waiting_for_region_area)

    else:
        keyboard = await cities_keyboard()
        await message.answer("Wrong! Please choose one of the two cities!", reply_markup=keyboard)


@dp.message(CommentState.waiting_for_city_area)
async def receive_city_area(message: Message, state: FSMContext):
    if message.text == "Back":
        back_button = KeyboardButton(text="Back")
        tashkent_city = KeyboardButton(text="Tashkent City")
        tashkent_region = KeyboardButton(text="Tashkent Region")
        keyboard = ReplyKeyboardMarkup(keyboard=[[tashkent_city], [tashkent_region], [back_button]],
                                       resize_keyboard=True)
        await message.answer("Please choose area!", reply_markup=keyboard)
        await state.set_state(CommentState.waiting_for_area)

    elif message.text == "Main Menu":
        await state.clear()
        menu = await main_menu()
        await message.answer("Returning to the main menu...", reply_markup=menu)

    elif message.text not in tashkent_city_areas:
        keyboard = await cities_menu()
        await message.answer("Invalid Command! Please choose an area from the list of areas!", reply_markup=keyboard)

    else:
        menu_jobs = await jobs_menu()
        await message.answer(f"Choose your job.", reply_markup=menu_jobs)
        await state.set_state(CommentState.waiting_for_job)


@dp.message(CommentState.waiting_for_region_area)
async def receive_region_area(message: Message, state: FSMContext):
    if message.text == "Back":
        back_button = KeyboardButton(text="Back")
        tashkent_city = KeyboardButton(text="Tashkent City")
        tashkent_region = KeyboardButton(text="Tashkent Region")
        keyboard = ReplyKeyboardMarkup(keyboard=[[tashkent_city], [tashkent_region], [back_button]],
                                       resize_keyboard=True)
        await message.answer("Please choose area!", reply_markup=keyboard)
        await state.set_state(CommentState.waiting_for_area)

    elif message.text == "Main Menu":
        await state.clear()
        menu = await main_menu()
        await message.answer("Returning to the main menu...", reply_markup=menu)

    elif message.text not in tashkent_region_areas:
        keyboard = await regions_menu()
        await message.answer("Invalid Command! Please choose an area from the list of areas!", reply_markup=keyboard)

    else:
        menu_jobs = await jobs_menu()
        await message.answer(f"Choose your job.", reply_markup=menu_jobs)
        await state.set_state(CommentState.waiting_for_job)


@dp.message(CommentState.waiting_for_job)
async def send_job(message: Message, state: FSMContext):
    if message.text == "Back":
        back_button = KeyboardButton(text="Back")
        tashkent_city = KeyboardButton(text="Tashkent City")
        tashkent_region = KeyboardButton(text="Tashkent Region")
        keyboard = ReplyKeyboardMarkup(keyboard=[[tashkent_city], [tashkent_region], [back_button]],
                                       resize_keyboard=True)
        await message.answer("Please choose area!", reply_markup=keyboard)
        await state.set_state(CommentState.waiting_for_area)

    elif message.text == "Main Menu":
        await state.clear()
        menu = await main_menu()
        await message.answer("Returning to the main menu...", reply_markup=menu)

    elif message.text == "Cook":
        text_cook = """
        Amirsaid Lavash is looking for good cooks

        Requirements:
        - age 18+
        - Man or Woman
        - Experience in cooking at least 1 year

        Conditions:
        - one day-off in a week
        - monthly competitive salary
        - breakfast and lunch are free
        - working with professionals

        For more information contact us:
        +998971234567
        +998999876543

        Working Days:
        Monday-Saturday 10:00-00:00
        Sunday Closed
        """
        photo_url = "https://imgur.com/a/PzssDUe"
        await message.answer_photo(photo_url, caption=text_cook)
        await message.answer("You can choose another job or press 'Back' to exit.", reply_markup=await jobs_menu())

    elif message.text == "Dish Washer":
        text_dish_washer = """
        Amirsaid Lavash is looking for dishwashers

        Requirements:
        - Age 18+
        - Man or Woman
        - Experience in dishwashing is preferred

        Conditions:
        - One day-off in a week
        - Monthly competitive salary
        - Breakfast and lunch are free
        - Working with professionals

        For more information contact us:
        +998971234567
        +998999876543

        Working Days:
        Monday-Saturday 10:00-00:00
        Sunday Closed
        """
        photo_url = "https://imgur.com/a/IzfxOuw"
        await message.answer_photo(photo_url, caption=text_dish_washer)
        await message.answer("You can choose another job or press 'Back' to exit.", reply_markup=await jobs_menu())

    elif message.text == "Cleaner":
        text_cleaner = """
        Amirsaid Lavash is looking for cleaners

        Requirements:
        - Age 18+
        - Man or Woman
        - Experience in cleaning is preferred

        Conditions:
        - One day-off in a week
        - Monthly competitive salary
        - Breakfast and lunch are free
        - Working with professionals

        For more information contact us:
        +998971234567
        +998999876543

        Working Days:
        Monday-Saturday 10:00-00:00
        Sunday Closed
        """
        photo_url = "https://imgur.com/a/dZ8ghz9"
        await message.answer_photo(photo_url, caption=text_cleaner)
        await message.answer("You can choose another job or press 'Back' to exit.", reply_markup=await jobs_menu())

    elif message.text == "Table cleaner":
        text_table_cleaner = """
        Amirsaid Lavash is looking for table cleaners

        Requirements:
        - Age 18+
        - Man or Woman
        - Experience in table cleaning is preferred

        Conditions:
        - One day-off in a week
        - Monthly competitive salary
        - Breakfast and lunch are free
        - Working with professionals

        For more information contact us:
        +998971234567
        +998999876543

        Working Days:
        Monday-Saturday 10:00-00:00
        Sunday Closed
        """
        photo_url = "https://imgur.com/a/6rvPiOL"
        await message.answer_photo(photo_url, caption=text_table_cleaner)
        await message.answer("You can choose another job or press 'Back' to exit.", reply_markup=await jobs_menu())

    elif message.text == "Barman":
        text_barman = """
        Amirsaid Lavash is looking for barmen

        Requirements:
        - Age 18+
        - Man or Woman
        - Experience in bartending is required

        Conditions:
        - One day-off in a week
        - Monthly competitive salary
        - Breakfast and lunch are free
        - Working with professionals

        For more information contact us:
        +998971234567
        +998999876543

        Working Days:
        Monday-Saturday 10:00-00:00
        Sunday Closed
        """
        photo_url = "https://imgur.com/a/aERzCT9"
        await message.answer_photo(photo_url, caption=text_barman)
        await message.answer("You can choose another job or press 'Back' to exit.", reply_markup=await jobs_menu())

    elif message.text == "Courier":
        text_courier = """
        Amirsaid Lavash is looking for couriers

        Requirements:
        - Age 18+
        - Man or Woman
        - Experience in delivery is preferred

        Conditions:
        - One day-off in a week
        - Monthly competitive salary
        - Breakfast and lunch are free
        - Working with professionals

        For more information contact us:
        +998971234567
        +998999876543

        Working Days:
        Monday-Saturday 10:00-00:00
        Sunday Closed
        """
        photo_url = "https://imgur.com/a/u4BZAZv"
        await message.answer_photo(photo_url, caption=text_courier)
        await message.answer("You can choose another job or press 'Back' to exit.", reply_markup=await jobs_menu())

    else:
        await message.answer("Invalid Command!", reply_markup=await jobs_menu())


@dp.message(F.text == "Menu 🍟")
async def send_menu(message: Message):
    photo_path = "https://imgur.com/a/quDcoY3"
    text = ("Bizning menu saytimiz orqali ko`rishingiz mumkin!"
            "https://oqtepalavash.uz/")
    await message.answer_photo(photo_path, caption=text)


@dp.message(F.text == "Comments and offers 💬")
async def send_comment(message: Message, state: FSMContext):
    back_button = KeyboardButton(text="Back")
    keyboard = ReplyKeyboardMarkup(keyboard=[[back_button]], resize_keyboard=True)
    await message.answer(
        "Please type your comment below. Press 'Back' to go to the main menu.",
        reply_markup=keyboard
    )
    await state.set_state(CommentState.waiting_for_comment)


@dp.message(CommentState.waiting_for_comment)
async def receive_comment(message: Message, state: FSMContext):
    if message.text == "Back":
        await state.clear()
        menu = await main_menu()
        await message.answer("Returning to the main menu...", reply_markup=menu)
    else:
        user_info = message.from_user
        comment = message.text
        await save_comment(user_info, comment)
        await message.answer("Thank you for your comment! Feel free to add another one.")


@dp.message(F.text == "Contacts and Address 📞")
async def send_contact(message: Message):
    text = """
    Call us right now!
    Our phone numbers:
    +998971234567
    +998999876543

    Working Days:
    Monday-Saturday 10:00-00:00
    Sunday Closed
    """
    latitude = 41.32579854695208
    longitude = 69.22872881905107
    await message.answer(text)
    await message.answer_location(text="This is our location", latitude=latitude, longitude=longitude)


@dp.message(F.text == "Language uzb/eng/rus")
async def send_language(message: Message):
    await message.answer("Unfortunately. We have only English language for now. Other languages will be added soon :)")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


