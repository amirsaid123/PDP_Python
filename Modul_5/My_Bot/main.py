from functions import *
from jobs import *

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
    photo_path = "https://imgur.com/a/quDcoY3"
    await message.answer_photo(photo_path, caption=text_about)

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
        photo_url = "https://imgur.com/a/PzssDUe"
        await message.answer_photo(photo_url, caption=text_cook)
        await message.answer("You can choose another job or press 'Back' to exit.", reply_markup=await jobs_menu())

    elif message.text == "Dish Washer":
        photo_url = "https://imgur.com/a/IzfxOuw"
        await message.answer_photo(photo_url, caption=text_dish_washer)
        await message.answer("You can choose another job or press 'Back' to exit.", reply_markup=await jobs_menu())

    elif message.text == "Cleaner":
        photo_url = "https://imgur.com/a/dZ8ghz9"
        await message.answer_photo(photo_url, caption=text_cleaner)
        await message.answer("You can choose another job or press 'Back' to exit.", reply_markup=await jobs_menu())

    elif message.text == "Table cleaner":
        photo_url = "https://imgur.com/a/6rvPiOL"
        await message.answer_photo(photo_url, caption=text_table_cleaner)
        await message.answer("You can choose another job or press 'Back' to exit.", reply_markup=await jobs_menu())

    elif message.text == "Barman":
        photo_url = "https://imgur.com/a/aERzCT9"
        await message.answer_photo(photo_url, caption=text_barman)
        await message.answer("You can choose another job or press 'Back' to exit.", reply_markup=await jobs_menu())

    elif message.text == "Courier":
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
    latitude = 41.32579854695208
    longitude = 69.22872881905107
    await message.answer(text_contact)
    await message.answer_location(text="This is our location", latitude=latitude, longitude=longitude)

@dp.message(F.text == "Language uzb/eng/rus")
async def send_language(message: Message):
    await message.answer("Unfortunately. We have only English language for now. Other languages will be added soon :)")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


