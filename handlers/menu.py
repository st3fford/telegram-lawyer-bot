from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda m: m.text == "ℹ️ Про бота")
async def about(message: Message):
    await message.answer(
        "🤖 Я допоможу вам:\n"
        "• записатись на консультацію\n"
        "• отримати зразки заяв\n"
        "• зв’язатись з оператором\n"
    )
