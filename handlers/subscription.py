from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import bot, faq
from db import users
from utils import SendGreeting
from utils.GetMessage import get_mes

router = Router()


@router.message(Command("subscription"))
async def subscription_handler(message: Message):
    id = message.from_user.id
    user = users.get(id=id)
    await bot.send_message(id=id,
                           text=get_mes("subscription",
                                        count_day=user.count_day,
                                        count_message=user.count_message,
                                        faq=faq,
                                        ref_link=user.ref_link))
    await SendGreeting.send(id)


subscription_rt = router
