# main.py
import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import start, menu, consultation, support
from handlers.free_text import router as free_text_router
from handlers.get_contact import router as contact_router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(consultation.router)
    dp.include_router(support.router)

    # 🔥 ДОДАЄМО НОВІ РОУТЕРИ
    dp.include_router(contact_router)
    dp.include_router(free_text_router)  # ставимо ОСТАННІМ

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())