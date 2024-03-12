from aiogram.filters import Filter
from aiogram.types import Message

from bot.db import users
from bot.db.Users import User


class IsUser(Filter):
    async def __call__(self, message: Message, event_from_user: User) -> bool:
        if event_from_user.id not in users:
            return True

        # user = users.get(event_from_user.id)
        # return bool(user.status)
