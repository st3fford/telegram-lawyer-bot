from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda m: m.text == "👤 Зв’язок з оператором")
async def support_chat(message: Message):
    await message.answer(
        "✍️ Опишіть вашу ситуацію.\n"
        "Оператор підключиться найближчим часом."
    )
