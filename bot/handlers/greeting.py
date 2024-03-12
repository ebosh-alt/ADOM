from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.config import bot, link_to_bot
from bot.db import users, User
from bot.utils import SendNotifications, SendGreeting
from bot.utils.GetMessage import get_mes
from bot import keyboards as kb

router = Router()


@router.message(Command("start"))
async def greeting_user(message: Message):
    id = message.from_user.id
    user = users.get(id=id)
    if user is None:
        user = users.add(User(id=id))
    user.username = message.from_user.username
    if user.username is None:
        await bot.send_message(text=get_mes("no_username"), reple_markup=kb.change_username)
        return 404
    await SendGreeting.send(id)


@router.callback_query(F.data == "change_username")
async def change_username(message: CallbackQuery):
    id = message.from_user.id
    user = users.get(id)
    user.username = message.from_user.username
    users.update(user)
    if user.username is None:
        await bot.edit_message_text(text=get_mes("no_username"),
                                    message_id=message.message.message_id,
                                    reple_markup=kb.change_username)
        return 404
    await SendGreeting.send(id)



greeting_rt = router