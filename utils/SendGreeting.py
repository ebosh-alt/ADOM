from aiogram.types import FSInputFile

from config import path_to_gret_photo, bot
from db import users, TypeSubscribes
import keyboards as kb
from utils.GetMessage import get_mes


async def send(id):
    user = users.get(id)
    photo = FSInputFile(path_to_gret_photo)
    if user.subscribe == TypeSubscribes.free_subscribe:
        keyboard = kb.subscribe_kb
        text = get_mes("greeting")
    else:
        keyboard = kb.faq_kb
        text = get_mes("greeting")

    await bot.send_photo(chat_id=id,
                         photo=photo,
                         caption=text,
                         reply_markup=keyboard)
