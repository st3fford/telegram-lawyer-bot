from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import os

router = Router()

OPERATOR_CHAT_ID = int(os.getenv("OPERATOR_CHAT_ID"))

@router.message()
async def free_text_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()

    # якщо користувач не в іншому сценарії
    if current_state is None:

        # форвардимо будь-який тип повідомлення
        await message.forward(OPERATOR_CHAT_ID)

        await message.answer(
            "✅ Ваше повідомлення передано оператору."
        )

