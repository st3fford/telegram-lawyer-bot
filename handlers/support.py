from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "👤 Зв’язок з оператором")
async def contact_operator(message: Message):
    await message.answer(
        "✍️ Опишіть вашу ситуацію.\n"
        "Ви можете надіслати текст, фото або документ.\n"
        "Оператор підключиться найближчим часом."
    )