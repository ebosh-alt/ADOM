from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def create_keyboard(name_buttons: list | dict, *sizes: int) -> types.InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    for name_button in name_buttons:
        if type(name_buttons[name_button]) is tuple:
            if len(name_buttons[name_button]) == 2:
                keyboard.button(
                    text=name_button, url=name_buttons[name_button][0], callback_data=name_buttons[name_button][1]
                )
            # else:
            #     if "http" in name_buttons[name_button]:
            #         keyboard.button(
            #             text=name_button, url=name_button
            #         )
            #     keyboard.button(
            #         text=name_button, callback_data=name_button
            #     )

        else:
            if "http" in str(name_buttons[name_button]):
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

subscribe_kb = create_keyboard({"1 неделя": "week",
                                "1 месяц": "month",
                                "6 месяцев": "half_year",
                                "Поддержка": "https://t.me/nikitaKwork"})

faq_kb = create_keyboard({"Поддержка": "https://t.me/nikitaKwork"})
