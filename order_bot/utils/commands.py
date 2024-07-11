from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="Старт"
        ),
        BotCommand(
            command="registration",
            description="Реєстрація"
        ),
        BotCommand(
            command="help",
            description="Допомога з ботом"
        ),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
