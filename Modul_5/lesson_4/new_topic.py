import json
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



TOKEN = "7968879091:AAHl4QXocWB9ItcbNS16vc0RtZhlTm7Zwoo"

if not TOKEN:
    raise ValueError("Bot token is not found in the .env file")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()



def make_button(btns_name : list , adjust: list):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[KeyboardButton(text = name) for name in btns_name])
    rkb.adjust(*adjust)
    return rkb.as_markup(resize_keyboard=True)

def accept():
    ikb = InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text = "✅ Accept" , callback_data="accept_file"),
        InlineKeyboardButton(text = "❌ Reject" , callback_data="reject_file")
    )
    ikb.adjust(2)
    return ikb.as_markup()

class CourseState(StatesGroup):
    course = State()
    fullname = State()
    group_name = State()
    exam_file = State()

recipient_user_id = 1148477816

courses = ["Python Backend", "Java Backend", "C++", "C", "C#", "PHP", "Flutter"]

@dp.message(CommandStart())
async def start_handler(message: Message, state:FSMContext) -> None:
    await message.bot.set_my_commands([BotCommand(command="/start", description="Start"),
                                       BotCommand(command="/help", description="Help")])
    courses = ["Python Backend", "Java Backend", "C++", "C", "C#", "PHP", "Flutter"]
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.answer(f"Please, choose your course!", reply_markup=make_button(courses, adjust=[2,2,2,1]))
    await state.set_state(CourseState.course)

@dp.message(CourseState.course)
async def course_hander(message: Message, state:FSMContext):
    if message.text not in courses:
        await message.answer("Invalid course! Please choose again!", reply_markup=make_button(courses))
        await state.set_state(CourseState.course)
    else:
        await state.set_data({"Course name": message.text})
        await message.answer("Enter your fullname", reply_markup=ReplyKeyboardRemove())
        await state.set_state(CourseState.fullname)

@dp.message(CourseState.fullname)
async def fullname_handler(message: Message, state:FSMContext):
    await state.update_data({"Fullname": message.text})
    await message.answer("Enter your group name", reply_markup=ReplyKeyboardRemove())
    await state.set_state(CourseState.group_name)

@dp.message(CourseState.group_name)
async def group_name_handler(message: Message, state:FSMContext):
    await state.update_data({"Group name": message.text})
    await message.answer("Send your exam file", reply_markup=ReplyKeyboardRemove())
    await state.set_state(CourseState.exam_file)

@dp.message(CourseState.exam_file, F.document)
async def exam_file_handler(message: Message, state:FSMContext):
    file_id = message.document.file_id
    file_name = message.document.file_name
    await state.update_data({"Exam file": file_name})
    data = await state.get_data()

    await message.answer("Your file has been saved :)")
    await state.clear()
    await message.answer(f"Your data {data}")
    await send_data_to_admin(data, file_id, bot)
    await message.answer("Your file has been sent!")



async def send_data_to_admin(data: dict, file_id: str, bot: Bot):
    try:
        formatted_data = "\n".join([f"{key}: {value}" for key, value in data.items()])
        buttons = await accept()


        message = await bot.send_document(
            chat_id=recipient_user_id,
            document=file_id,
            caption=f"New submission:\n\n{formatted_data}",
            reply_markup=buttons
        )

        submitted_data[message.message_id] = {
            "data": data,
            "file_id": file_id
        }
    except Exception as e:
        logging.error(f"Failed to send data to admin: {e}")


submitted_data = {}

@dp.callback_query(lambda c: c.data in ["accept_file", "reject_file"])
async def process_admin_decision(callback: CallbackQuery):
    message_id = callback.message.message_id
    if callback.data == "accept_file":
        await callback.message.edit_caption(
            caption=f"{callback.message.caption}\n\n✅ File has been accepted."
        )
        await callback.answer("You accepted the file.")
    elif callback.data == "reject_file":
        if message_id in submitted_data:
            del submitted_data[message_id]
        await callback.message.delete()
        await callback.answer("You rejected and deleted the file.")



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


