from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from order_bot.keyboards.back_kb import back_kb
from order_bot.keyboards.profile_kb import profile_kb
from order_bot.state.change_name import ChangeUserName
from order_bot.state.change_phone import ChangeUserPhone
from order_bot.utils.db_utils import user_update_phone, user_update_name


async def start_change_name(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await bot.send_message(message.from_user.id, "Давай змінемо💫")

    await bot.send_message(
        message.from_user.id,
        f"Вкажи нове ім'я",
        reply_markup=back_kb
    )
    await state.set_state(ChangeUserName.first_name)


async def set_new_name(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await state.update_data(regname=message.text)
    reg_data = await state.get_data()
    reg_name = reg_data.get("regname")

    await user_update_name(
        user_telegram_id=message.from_user.id,
        user_first_name=reg_name
    )
    await bot.send_message(
        message.from_user.id,
        f"Змінив твоє імя на: \n"
        f"{reg_name}",
        reply_markup=profile_kb
    )
    await state.clear()


async def start_change_phone(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await bot.send_message(message.from_user.id, "Давай змінемо💫")

    await bot.send_message(
        message.from_user.id,
        f"📞Вкажіть свій номер у форматі: 0951112233",
        reply_markup=back_kb
    )
    await state.set_state(ChangeUserPhone.phone_number)


async def set_new_phone(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    phone_number = message.text.strip()
    if len(phone_number) == 10 and phone_number.isdigit():
        await state.update_data(regphone=message.text)
        reg_data = await state.get_data()
        reg_phone = reg_data.get("regphone")

        await user_update_phone(
            user_telegram_id=message.from_user.id,
            user_phone=reg_phone
        )

        await bot.send_message(
            message.from_user.id,
            f"Змінив твій номер на: \n"
            f" {reg_phone}",
            reply_markup=profile_kb
        )
        await state.clear()
    else:
        await bot.send_message(
            message.from_user.id,
            "Вказан не вірний номер телефону. Спробуй ще."
        )
        await state.clear()

