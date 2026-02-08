# main.py
import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import start, menu, consultation, support


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(consultation.router)
    dp.include_router(support.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
