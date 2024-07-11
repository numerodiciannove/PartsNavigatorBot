from aiogram import Bot
from aiogram.types import (
    Message,
    CallbackQuery
)
from aiogram.fsm.context import FSMContext

from order_bot.handlers.add_car import add_vin_code_start
from order_bot.handlers.registration import start_register
from order_bot.keyboards.choose_my_car_for_detail_kb import user_cars_kb
from order_bot.utils.check_if_user_exist import handle_user_existence
from order_bot.utils.db_utils import get_user_cars_sync, create_order_db
from users.models import SalesDepartment

from asgiref.sync import sync_to_async


async def start_create_detail_order(
        message: Message,
        state: FSMContext,
        bot: Bot
):
    await state.clear()
    telegram_user_id = message.from_user.id
    user_exists = await handle_user_existence(telegram_user_id)
    user_cars = await get_user_cars_sync(telegram_user_id)

    if user_exists:
        if user_cars:
            keyboard_markup = await user_cars_kb(telegram_user_id)
            await bot.send_message(
                message.from_user.id,
                "Оберіть 🚙 авто:",
                reply_markup=keyboard_markup
            )
        else:
            await bot.send_message(
                message.from_user.id,
                "У вас ще немає доданих авто."
            )

            await add_vin_code_start(
                message=message,
                state=state,
                bot=bot
            )
    else:
        await bot.send_message(
            message.from_user.id,
            "Для початку треба зареєструватись...",
        )
        await start_register(message, state, bot)


async def create_repair_order(
        callback_query: CallbackQuery,
        state: FSMContext,
):
    await state.clear()
    vin_code = callback_query.data[len('create_repair_order_'):]
    print(vin_code)

    try:
        sales_department = await sync_to_async(
            SalesDepartment.objects.get
        )(name="Repair")
    except SalesDepartment.DoesNotExist:
        await callback_query.message.edit_text(
            f"Відділ 'Repair' не знайдено.",
        )
        await callback_query.answer()
        return

    if vin_code:
        order = await create_order_db(
            vin_code=vin_code,
            sales_department=sales_department
        )
        await callback_query.message.edit_reply_markup(reply_markup=None)
        if order:
            await callback_query.message.answer(
                f"👌 Створено нове замовлення, для вашого авто: \n\n"
                f"🚙 VIN - {vin_code}\n\n"
                f"Cкоро наш менеджер зв'яжется з вами!",
            )
        else:
            await callback_query.message.edit_text(
                f"Не вдалось створити заповленя.",
            )
    else:
        await callback_query.message.edit_text(
            f"Не вдалось створити замовленя.",
        )

    await callback_query.answer()


async def create_detail_order(
        callback_query: CallbackQuery,
        state: FSMContext
):
    await state.clear()
    vin_code = callback_query.data[len('create_detail_order_'):]
    print(vin_code)

    try:
        sales_department = await sync_to_async(
            SalesDepartment.objects.get
        )(name="Detail")
    except SalesDepartment.DoesNotExist:
        await callback_query.message.edit_text(
            f"Відділ 'Detail' не знайдено.",
        )
        await callback_query.answer()
        return

    if vin_code:
        order = await create_order_db(
            vin_code=vin_code,
            sales_department=sales_department
        )
        await callback_query.message.edit_reply_markup(reply_markup=None)
        if order:
            await callback_query.message.answer(
                f"👌 Створено нове замовлення, для вашого авто: \n\n"
                f"🚙 VIN - {vin_code}\n\n"
                f"Cкоро наш менеджер зв'яжется з вами!",
            )
        else:
            await callback_query.message.edit_text(
                f"Не вдалось створити заповленя.",
            )
    else:
        await callback_query.message.edit_text(
            f"Не вдалось створити замовленя.",
        )

    await callback_query.answer()
