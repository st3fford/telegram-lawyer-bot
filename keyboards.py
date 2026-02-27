from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Запис на консультацію")],
        [KeyboardButton(text="📄 Зразки заяв")],
        [KeyboardButton(text="👤 Зв’язок з оператором")],
        [KeyboardButton(text="📞 Поділитись контактом", request_contact=True)]
    ],
    resize_keyboard=True
)