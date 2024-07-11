from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from order_bot.keyboards.profile_kb import profile_kb


async def go_to_profile(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    await bot.send_message(
        message.from_user.id,
        f"Обери далі...",
        reply_markup=profile_kb
    )
