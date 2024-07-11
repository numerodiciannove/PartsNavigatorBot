from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from order_bot.handlers.registration import start_register
from order_bot.keyboards.back_kb import back_kb
from order_bot.keyboards.profile_kb import profile_kb
from order_bot.state.vin_code import RegisterVinCode
from order_bot.utils.check_if_user_exist import handle_user_existence
from order_bot.utils.db_utils import add_new_vin_code


async def add_vin_code_start(message: Message, state: FSMContext, bot: Bot):
    telegram_id = message.from_user.id
    user_exists = await handle_user_existence(telegram_id)

    if user_exists:
        await bot.send_message(
            message.from_user.id,
            "Укажите 17-значный VIN-код:",
            reply_markup=back_kb
        )
        await state.set_state(RegisterVinCode.vin_code)
    else:
        await bot.send_message(
            message.from_user.id,
            "Для початку треба зареєструватись...",
        )
        await start_register(message, state, bot)


async def process_vin_code(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    vin_code = message.text.strip().upper()
    if len(vin_code) == 17:
        await state.update_data(vin_code=vin_code)
        reg_data = await state.get_data()
        reg_vin = reg_data.get("vin_code")
        msg = "Перевіряю..."
        await bot.send_message(
            message.from_user.id, msg, reply_markup=back_kb
        )

        car = await add_new_vin_code(
            telegram_id=message.from_user.id,
            vin_code=reg_vin
        )

        if car:
            await bot.send_message(
                message.from_user.id,
                f"Все добре!👌\n\n"
                f"✅ Ваш VIN-код був успішно збережений!\n\n"
                f"🚙 VIN - {car.vin_code}",
                reply_markup=profile_kb

            )
        else:
            await bot.send_message(
                message.from_user.id,
                f"Не вдалося знайти користувача. Будь ласка, зареєструйтесь.",
            )

        await state.clear()
    else:
        await bot.send_message(
            message.from_user.id,
            "⚠️ Вказано не вірний VIN-код. Він повинен містити 17 символів.\n\n"
        )

        await state.clear()

        await add_vin_code_start(
            message,
            state,
            bot
        )
