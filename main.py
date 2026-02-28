# main.py

import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

# Основні хендлери
from handlers import start, menu

# Контакт
from handlers.get_contact import router as contact_router

# Форвард повідомлень клієнта
from handlers.free_text import router as free_text_router

# Reply з групи операторів
from handlers.group_reply import router as group_reply_router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # 🔹 1. Базові команди
    dp.include_router(start.router)
    dp.include_router(menu.router)

    # 🔹 2. Контакт
    dp.include_router(contact_router)

    # 🔹 3. Reply з групи (ВАЖЛИВО — перед free_text)
    dp.include_router(group_reply_router)

    # 🔹 4. Форвард повідомлень клієнта (останній)
    dp.include_router(free_text_router)

    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())