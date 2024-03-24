from aiogram import Dispatcher, Bot

api_key = "6179616567:AAGz4ykh1SgXq_EAKTb_lU1jZpyfhp8BOSY"

dp = Dispatcher()
bot = Bot(api_key, parse_mode="Markdown")
link_to_bot = "https://t.me/ADOMs_bot"
name_bot = "ADOM"
path_to_gret_photo = "db/gret_photo.jpg"
path_to_help_video = "db/feedback.mp4"

# оплата
pay_api_key = "test_511rSJnFSegQXRuIu-4uRhntXSTH-aUqv6vE6En0srk"
pay_shopId = 349969
pay_token = "381764678:TEST:80295"

# перенести в messages
payment_title = f"{name_bot}: VIP"
payment_description = "Пакет VIP для {username}"
success_payment = "УРА! Пакет куплен"

faq = "@nikitaKwork"
ref_award_day = 2
ref_award_message = 20
