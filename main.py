import asyncio
import sys

from contextlib import suppress
import logging
from handlers import routers
from config import bot, dp


async def main() -> None:
    for router in routers:
        dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        # filemode="w",
                        format="%(levelname)s %(asctime)s %(message)s",
                        encoding='utf-8')
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
