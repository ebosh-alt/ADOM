from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from config import faq
from db import TypeAI


def create_keyboard(name_buttons: list | dict, *sizes: int) -> types.InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    if type(name_buttons) is list:
        for name_button in name_buttons:
            keyboard.button(
                text=name_button, callback_data=name_button
            )
    elif type(name_buttons) is dict:
        for name_button in name_buttons:
            if "http" in name_buttons[name_button] or "@" in name_buttons[name_button]:
                keyboard.button(
                    text=name_button, url=name_buttons[name_button]
                )
            else:
                keyboard.button(
                    text=name_button, callback_data=name_buttons[name_button]
                )

    if len(sizes) == 0:
        sizes = (1,)
    keyboard.adjust(*sizes)
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True)


def create_reply_keyboard(name_buttons: list, one_time_keyboard: bool = False, request_contact: bool = False,
                          *sizes) -> types.ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()

    for name_button in name_buttons:
        keyboard.button(
            text=name_button,
            request_contact=request_contact

        )
    if len(sizes) == 0:
        sizes = (1,)
    keyboard.adjust(*sizes)
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=one_time_keyboard)


del_mes_kb = create_keyboard({"Удалить уведомление": "del_notification"})

change_username = create_keyboard({"Готово": "change_username"})

subscribe_button = {"1 неделя": "1 неделя",
                    "1 месяц": "1 месяц",
                    "6 месяцев": "6 месяцев",
                    "Поддержка": "https://t.me/nikitaKwork"}

subscribe_kb = create_keyboard(subscribe_button)

faq_kb = create_keyboard({"Поддержка": faq})

help_kb = create_keyboard([TypeAI.write, TypeAI.say])

if __name__ == "__main__":
    print(subscribe_button.values())
