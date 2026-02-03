# main.py
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from config import BOT_TOKEN
from keyboards import main_menu
from operators import router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    @dp.message(CommandStart())
    async def start(message: types.Message):
        await message.answer(
            "Вітаємо! 👋\nОберіть дію з меню нижче:",
            reply_markup=main_menu()
        )

    @dp.message()
    async def fallback(message: types.Message):
        await message.answer(
            "Будь ласка, скористайтесь меню 👇",
            reply_markup=main_menu()
        )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
