from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import os

router = Router()

OPERATOR_CHAT_ID = int(os.getenv("OPERATOR_CHAT_ID"))

@router.message(F.text)
async def free_text_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is None:
        text = (
            "📩 НОВЕ ПОВІДОМЛЕННЯ ВІД КЛІЄНТА\n\n"
            f"👤 {message.from_user.full_name}\n"
            f"🆔 ID: {message.from_user.id}\n\n"
            f"💬 {message.text}"
        )

        await message.bot.send_message(OPERATOR_CHAT_ID, text)

        await message.answer(
            "✅ Ваше повідомлення передано оператору."
        )