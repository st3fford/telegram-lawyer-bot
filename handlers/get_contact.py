from aiogram import Router, F
from aiogram.types import Message
import os

router = Router()

OPERATOR_CHAT_ID = int(os.getenv("OPERATOR_CHAT_ID"))

@router.message(F.contact)
async def contact_handler(message: Message):

    # перевірка що це власний контакт
    if message.contact.user_id != message.from_user.id:
        await message.answer("❌ Будь ласка, надішліть власний контакт.")
        return

    text = (
        "📞 КЛІЄНТ ПОДІЛИВСЯ КОНТАКТОМ\n\n"
        f"👤 Імʼя: {message.contact.first_name}\n"
        f"📱 Телефон: {message.contact.phone_number}\n"
        f"🆔 Telegram ID: {message.from_user.id}"
    )

    await message.bot.send_message(OPERATOR_CHAT_ID, text)

    await message.answer("✅ Дякуємо! Ваш номер передано адвокату.")