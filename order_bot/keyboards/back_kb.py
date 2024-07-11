from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙 Повернутись до профілю"),
            KeyboardButton(text="🔙 Повернутись до меню"),
        ],
    ],
    resize_keyboard=True,
)
