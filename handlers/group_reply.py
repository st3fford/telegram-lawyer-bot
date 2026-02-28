from aiogram import Router, F
from aiogram.types import Message
import os

router = Router()

OPERATOR_CHAT_ID = int(os.getenv("OPERATOR_CHAT_ID"))

@router.message(F.reply_to_message)
async def reply_from_group(message: Message):

    # працюємо тільки в операторській групі
    if message.chat.id != OPERATOR_CHAT_ID:
        return

    # перевіряємо що це відповідь на форвард
    if not message.reply_to_message.forward_from:
        return

    user_id = message.reply_to_message.forward_from.id

    # копіюємо будь-який тип повідомлення
    await message.copy_to(user_id)