import logging

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot import keyboards as kb
from bot.config import bot, pay_token, success_payment, payment_title, payment_description
from bot.db import users, Prices, TypeSubscribes, CountMessageSubscribes, CountDaySubscribes
from bot.states import States

router = Router()


@router.callback_query(F.data.in_(kb.subscribe_button.values()))
async def start_payment(message: CallbackQuery, state: FSMContext):
    id = message.from_user.id
    user = users.get(id)
    prices = None
    payload = None
    await state.set_state(States.payment)
    match message.data:
        case TypeSubscribes.week_subscribe:
            prices = [types.LabeledPrice(label=TypeSubscribes.week_subscribe, amount=Prices.week_subscribe)]
            payload = TypeSubscribes.week_subscribe
            await state.update_data(count_message=CountMessageSubscribes.week_subscribe,
                                    count_day=CountDaySubscribes.week_subscribe,
                                    type_subscribe=TypeSubscribes.week_subscribe)

        case TypeSubscribes.month_subscribe:
            prices = [types.LabeledPrice(label=TypeSubscribes.month_subscribe, amount=Prices.month_subscribe)]
            payload = TypeSubscribes.month_subscribe
            await state.update_data(count_message=CountMessageSubscribes.month_subscribe,
                                    count_day=CountDaySubscribes.month_subscribe,
                                    type_subscribe=TypeSubscribes.month_subscribe)

        case TypeSubscribes.half_year_subscribe:
            prices = [types.LabeledPrice(label=TypeSubscribes.half_year_subscribe, amount=Prices.half_year_subscribe)]
            payload = TypeSubscribes.half_year_subscribe
            await state.update_data(count_message=CountMessageSubscribes.half_year_subscribe,
                                    count_day=CountDaySubscribes.half_year_subscribe,
                                    type_subscribe=TypeSubscribes.half_year_subscribe)

    await bot.send_invoice(
        chat_id=id,
        title=payment_title,
        description=payment_description.format(username=f"@{user.username}"),
        provider_token=pay_token,
        currency='rub',
        prices=prices,
        start_parameter='Subscribe',
        payload=payload
    )


@router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    logging.info("Processing pre-checkout query")
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@router.message(F.successful_payment)
async def successful_payment(message: Message, state: FSMContext):
    logging.info(message.successful_payment)
    id = message.from_user.id
    user = users.get(id)
    data = await state.get_data()
    count_message = data.get('count_message', 0)
    count_day = data.get('count_day', 0)
    user.count_day = count_day
    user.count_message = count_message
    user.subscribe = data.get('type_subscribe', TypeSubscribes.free_subscribe)
    users.update(user)
    await bot.send_message(
        chat_id=id,
        text=success_payment)


payments_rt = router
