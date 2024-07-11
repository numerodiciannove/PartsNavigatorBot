from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛠Замовити ремонт"),
            KeyboardButton(text="🚘Замовити деталь")
        ],
        [
            KeyboardButton(text="😎Мій профіль"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Натисни на кнопку нижче. 💫"
)
