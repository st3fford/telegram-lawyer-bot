from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.startswith("/reply"))
async def reply_to_client(message: Message):

    parts = message.text.split(" ", 2)

    if len(parts) < 3:
        await message.answer("Формат: /reply user_id текст")
        return

    try:
        user_id = int(parts[1])
    except ValueError:
        await message.answer("Невірний user_id")
        return

    text = parts[2]

    await message.bot.send_message(user_id, text)
    await message.answer("✅ Відповідь надіслано клієнту")