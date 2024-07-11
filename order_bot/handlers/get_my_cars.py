from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from order_bot.keyboards.profile_kb import profile_kb
from order_bot.utils.db_utils import fetch_user_cars


async def get_cars(message: Message, bot: Bot, state: FSMContext):
    await state.clear()

    user_cars = await fetch_user_cars(telegram_user_id=message.from_user.id)

    if user_cars:
        cars_list = "\n".join([f"🚙 {car.vin_code}" for car in user_cars])
        await bot.send_message(
            message.from_user.id,
            f"Ваші авто: \n\n"
            f"{cars_list}",
            reply_markup=profile_kb
        )
    else:
        await bot.send_message(
            message.from_user.id,
            "У вас еще нет добавленных автомобилей.",
            reply_markup=profile_kb
        )

    await state.clear()
