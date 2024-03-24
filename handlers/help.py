from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile

from config import bot, path_to_help_video
from db import users, User, TypeAI
from utils.GetMessage import get_mes
import keyboards as kb

router = Router()


@router.message(Command("help"))
async def help_handler(message: Message):
    id = message.from_user.id
    user = users.get(id=id)
    buttons = []
    match user.type_ai:
        case TypeAI.write:
            buttons.append(f"👉{TypeAI.write}👈")
            buttons.append(TypeAI.say)
        case TypeAI.say:
            buttons.append(TypeAI.write)
            buttons.append(f"👉{TypeAI.say}👈")

    video = FSInputFile(path_to_help_video)
    await bot.send_video(chat_id=id,
                         video=video,
                         caption=get_mes("help"),
                         reply_markup=kb.create_keyboard(buttons))


@router.callback_query(F.data.contains(TypeAI.write) | F.data.contains(TypeAI.say))
async def change_type_ai(message: CallbackQuery):
    id = message.from_user.id
    user = users.get(id)
    buttons = []
    match message.data.replace("👉", "").replace("👈", ""):
        case TypeAI.write:
            user.type_ai = TypeAI.write
            buttons.append(f"👉{TypeAI.write}👈")
            buttons.append(TypeAI.say)
        case TypeAI.say:
            user.type_ai = TypeAI.say
            buttons.append(TypeAI.write)
            buttons.append(f"👉{TypeAI.say}👈")
    await message.message.delete()
    users.update(user)
    video = FSInputFile(path_to_help_video)
    await bot.send_video(chat_id=id,
                         message_id=message.message.message_id,
                         media=video,
                         caption=get_mes("help"),
                         reply_markup=kb.create_keyboard(buttons))


help_rt = router
