from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Запис на консультацію")],
        [KeyboardButton(text="📄 Зразки заяв")],
        [KeyboardButton(text="👤 Зв’язок з оператором")],
        [KeyboardButton(text="🤖 Юридичний GPT")],
        [KeyboardButton(text="ℹ️ Про бота")]
    ],
    resize_keyboard=True
)

