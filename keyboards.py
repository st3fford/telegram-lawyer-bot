# keyboards.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📞 Поділитись номером", request_contact=True)],
            [KeyboardButton(text="👨‍⚖️ Зв'язок з оператором")],
            [KeyboardButton(text="📅 Записатись на консультацію")],
        ],
        resize_keyboard=True
    )
