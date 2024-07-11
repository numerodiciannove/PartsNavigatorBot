from aiogram import Bot
from aiogram.types import Message
from order_bot.keyboards.main_kb import main_kb
from order_bot.keyboards.register_kb import register_keyboard
from order_bot.utils.db_utils import get_user_by_telegram_id


async def get_start(message: Message, bot: Bot):
    user = await get_user_by_telegram_id(message.from_user.id)

    if not user:
        hello_text = (
            f"Вітаю👋!\n"
            f"Мене звати 🚘PartsNavigatorBot.\n\n"
            f"Щоб робити замовлення з початку треба пройти швидку реєстрацію. \n\n"
            f"💫\n"
            f"Для початку реєстрації натисні:\n"
            f"/registration\n"
        )
        await bot.send_message(
            message.from_user.id, hello_text, reply_markup=register_keyboard
        )
    else:
        await bot.send_message(
            message.from_user.id,
            f"Вітаю, {user.first_name}👋!",
            reply_markup=main_kb
        )
