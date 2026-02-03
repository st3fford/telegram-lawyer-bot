# operators.py
from aiogram import Router, types
from config import OPERATORS

router = Router()


@router.message(lambda msg: msg.text == "👨‍⚖️ Зв'язок з оператором")
async def connect_operator(message: types.Message):
    for operator_id in OPERATORS:
        await message.bot.send_message(
            operator_id,
            f"🆕 Новий запит від користувача:\n"
            f"👤 @{message.from_user.username}\n"
            f"🆔 {message.from_user.id}"
        )

    await message.answer("✅ Оператор отримав ваш запит і скоро напише вам.")
