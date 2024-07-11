import django

import asyncio
import logging
import os

from aiogram import Dispatcher, Bot, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from dotenv import load_dotenv

from order_bot.handlers.add_car import process_vin_code, add_vin_code_start
from order_bot.handlers.create_detail_order import start_create_detail_order
from order_bot.handlers.create_repair_order import (
    create_repair_order,
    create_detail_order, start_create_repair_order
)
from order_bot.handlers.delete_car import start_delete_auto, delete_car
from order_bot.handlers.edit_user import (
    start_change_name,
    set_new_name,
    start_change_phone,
    set_new_phone
)
from order_bot.handlers.get_my_cars import get_cars
from order_bot.handlers.help import get_help
from order_bot.handlers.menu import go_to_main_menu
from order_bot.handlers.my_profile import go_to_profile
from order_bot.handlers.registration import (
    start_register,
    register_name,
    register_phone
)
from order_bot.handlers.start import get_start
from order_bot.state.change_name import ChangeUserName
from order_bot.state.change_phone import ChangeUserPhone
from order_bot.state.register import RegisterState
from order_bot.state.vin_code import RegisterVinCode
from order_bot.utils.commands import set_commands

django.setup()
load_dotenv()

ADMIN_ID = os.environ["ADMIN_ID"]
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()


# Send a message to admin when bot started
async def start_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text="Bot started!")


# Start message
dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands="start"))

# Help
dp.message.register(get_help, Command(commands="help"))

# Register user
dp.message.register(start_register, Command(commands="registration"))
dp.message.register(register_name, RegisterState.first_name)
dp.message.register(register_phone, RegisterState.phone_number)

# Menu
dp.message.register(go_to_profile, F.text == "😎Мій профіль")
dp.message.register(go_to_profile, F.text == "🔙 Повернутись до профілю")

# Profile
dp.message.register(add_vin_code_start, F.text == "✅Додати авто")
dp.message.register(go_to_main_menu, F.text == "🔙 Виберіть послугу")

# Add car
dp.message.register(process_vin_code, RegisterVinCode.vin_code)

# Add repair order
dp.message.register(start_create_repair_order, F.text == "🛠Замовити ремонт")
dp.callback_query.register(
    create_repair_order, lambda c: c.data.startswith('create_repair_order')
)

# Add detail order
dp.message.register(start_create_detail_order, F.text == "🚘Замовити деталь")
dp.callback_query.register(
    create_detail_order, lambda c: c.data.startswith('create_detail_order')
)


# Get user cars
dp.message.register(get_cars, F.text == "🚙Мої авто")

# Delete car
dp.message.register(start_delete_auto, F.text == "❌Видалити авто")
dp.callback_query.register(delete_car, lambda c: c.data.startswith('delete_car'))

# Change username
dp.message.register(start_change_name, F.text == "✍️Змінити ім'я")
dp.message.register(set_new_name, ChangeUserName.first_name)

# Change user phone
dp.message.register(start_change_phone, F.text == "✍️Змінити номер телефону")
dp.message.register(set_new_phone, ChangeUserPhone.phone_number)


async def main():
    # Menu commands
    await set_commands(bot)

    logging.basicConfig(level=logging.INFO)

    try:
        await dp.start_polling(bot, skip_update=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
