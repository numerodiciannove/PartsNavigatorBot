from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profile_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚙Мої авто"),
        ],
        [
            KeyboardButton(text="✅Додати авто"),
            KeyboardButton(text="❌Видалити авто"),
        ],
        [
            KeyboardButton(text="✍️Змінити ім'я"),
            KeyboardButton(text="✍️Змінити номер телефону"),
        ],
        [
        KeyboardButton(text="🔙 Виберіть послугу"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Натисни на кнопку нижче. 💫"
)
