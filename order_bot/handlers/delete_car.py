from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from order_bot.keyboards.delete_car_kb import user_cars_kb

from order_bot.keyboards.profile_kb import profile_kb
from order_bot.utils.db_utils import delete_car_by_vin_code, get_user_cars_sync


async def start_delete_auto(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    telegram_user_id = message.from_user.id
    user_cars = await get_user_cars_sync(telegram_user_id)

    if user_cars:
        keyboard_markup = await user_cars_kb(telegram_user_id)
        await bot.send_message(
            message.from_user.id,
            "Оберіть авто, яке ви хочете видалити:",
            reply_markup=keyboard_markup
        )
    else:
        await bot.send_message(
            message.from_user.id,
            "У вас ще немає доданих авто для видалення."
        )


async def delete_car(callback_query: CallbackQuery):
    vin_code = callback_query.data[len('delete_car_'):]

    if vin_code:
        await delete_car_by_vin_code(vin_code=vin_code)
        await callback_query.message.edit_reply_markup(reply_markup=None)
        await callback_query.answer(
            f"❌ VIN - {vin_code} видалено!",
            show_alert=True,
            reply_markup=profile_kb
        )
    else:
        await callback_query.message.edit_text(
            f"Не вдалось знайти авто для видалення.",
            reply_markup=profile_kb
        )

    await callback_query.answer()
