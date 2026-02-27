# main.py
import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

# Імпортуємо всі роутери
from handlers import start, menu, consultation, support
from handlers.get_contact import router as contact_router
from handlers.free_text import router as free_text_router
from handlers.operator_reply import router as operator_reply_router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Основні хендлери
    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(consultation.router)
    dp.include_router(support.router)

    # 🔹 Обробка контакту
    dp.include_router(contact_router)

    # 🔹 Команда /reply для оператора
    dp.include_router(operator_reply_router)

    # 🔹 Free text ставимо ОСТАННІМ
    dp.include_router(free_text_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())