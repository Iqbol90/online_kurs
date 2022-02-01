from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(commands="info_html")
async def bot_help(message: types.Message):
    text = f"Assalomu alaykum, {message.from_user.full_name}!\n"
    text+="Bu <b>qalin matn.</b>\n"
    text+="Bu <i>egri matn.</i>\n"
    text+="Bu <u>ostiga chizilgan matn.</u>\n"
    text+="Bu <s>o'chirilgan matn.</s>\n"
    text+="Bu <a href='https://mohirdev.uz'>linkni ulashish.</a>\n"
    text+="Bu <code>print('Hello World!')</code> kod. \n"

    await message.answer(text)

