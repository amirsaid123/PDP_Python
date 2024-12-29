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
from aiogram.utils.i18n import gettext as _, I18n, FSMI18nMiddleware
from aiogram.utils.i18n import lazy_gettext as __



TOKEN = "7026470459:AAFut-PH00ZXVuG5cdPN-xQ6TBGxTE7Kq4g"


if not TOKEN:
    raise ValueError("Bot token is not found in the .env file")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

class ButtonState(StatesGroup):
    lang = State()

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
async def command_start_handler(message: Message) -> None:
    buttons = [
        _("🏢 Kompaniya haqida"),
        _("📍 Fililallar"),
        _("💼 Bo'sh ish o'rinlari"),
        _("Menyu"),
        _("🗣 Yangiliklar"),
        _("📞 Kontaktlar/Manzil"),
        _("Til")
    ]
    ad_just = [2,1,2,2]
    await message.answer("Menu", reply_markup=make_keyboard_button(buttons, ad_just))



@dp.message(F.text == __("Til"))
async def lang_handler(message : Message , state : FSMContext):
    buttons = ["🇷🇺 Русский" , "🇺🇿 O'zbekcha" , "🇺🇸 English" , _("Ortga")]
    ad_just = [3,1]
    await state.set_state(ButtonState.lang)
    await message.answer(_("Maqul tilni tanlang") , reply_markup=make_keyboard_button(buttons , ad_just))


@dp.message(ButtonState.lang)
async def lang_handler(message : Message , state : FSMContext , i18n):
    lang = {
        "🇷🇺 Русский" : "ru",
        "🇺🇿 O'zbekcha" : "uz",
        "🇺🇸 English" : "en",

    }
    code = lang.get(message.text)
    await state.set_data({"locale" :code })
    i18n.current_locale = code
    buttons = [
        _("🏢 Kompaniya haqida"),
        _("📍 Fililallar"),
        _("💼 Bo'sh ish o'rinlari"),
        _("Menyu"),
        _("🗣 Yangiliklar"),
        _("📞 Kontaktlar/Manzil"),
        _("Til")
    ]
    ad_just = [2, 1, 2, 2]
    await message.answer(_("Til o'zgardi !") , reply_markup=make_keyboard_button(buttons , ad_just))









async def main() -> None:
    i18n = I18n(path="locales", default_locale="uz", domain="messages")
    dp.update.middleware(FSMI18nMiddleware(i18n))
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


