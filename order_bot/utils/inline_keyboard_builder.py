from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class InlineKeyboardBuilder:
    def __init__(self):
        self.keyboard = []

    def button(self, text, callback_data):
        self.keyboard.append(
            [InlineKeyboardButton(text=text, callback_data=callback_data)])

    def adjust(self, columns):
        while len(self.keyboard) % columns != 0:
            self.keyboard.append([])

    def as_markup(self):
        return InlineKeyboardMarkup(inline_keyboard=self.keyboard)
