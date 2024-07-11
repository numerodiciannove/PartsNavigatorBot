from aiogram import Bot
from aiogram.types import Message


async def get_help(message: Message, bot: Bot):
    help_text = (
        f"Вітаю!👋\n"
        f"Мене звати 🚘PartsNavigatorBot.\n\n"
    )
    await bot.send_message(
        message.from_user.id, help_text,
    )
