import logging

from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from order_bot.keyboards.main_kb import main_kb
from order_bot.state.register import RegisterState
from asgiref.sync import sync_to_async
from order_bot.utils.db_utils import get_user_by_telegram_id
from users.models import Client

logger = logging.getLogger(__name__)


async def start_register(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    user = await get_user_by_telegram_id(message.from_user.id)
    if user:
        await bot.send_message(
            message.from_user.id,
            f"Ааа все! 🤓 \n\n{user.first_name} - 📞{user.phone_number} вже зареєстрован!",
            reply_markup=main_kb
        )
    else:
        await bot.send_message(message.from_user.id, "Давай почнемо💫")
        await bot.send_message(
            message.from_user.id,
            "Як вас звати?",
            reply_markup=None
        )
        await state.set_state(RegisterState.first_name)


async def register_name(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f"Рад знайомству😌, {message.text}!"
    )
    await bot.send_message(
        message.from_user.id,
        f"Зараз треба вказати свій номер телефону, "
        f"щоб наші менеджери змогли зв'язатись з вами та допомогати з вашими заповленями. \n\n"
        f"📞Вкажіть свій номер у форматі: 0951112233\n",
        reply_markup=None
    )
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.phone_number)


async def register_phone(message: Message, state: FSMContext, bot: Bot):
    phone_number = message.text.strip()
    if len(phone_number) == 10 and phone_number.isdigit():
        await state.update_data(regphone=message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get("regname")
        reg_phone = reg_data.get("regphone")
        msg = f"Все добре!👌\n\n Ви вказали: \n 😎{reg_name} \n 📞{reg_phone}"
        await bot.send_message(
            message.from_user.id, msg, reply_markup=main_kb
        )

        telegram_username = message.from_user.username

        if message.from_user.username is None:
            telegram_username = reg_phone

        await create_user(
            first_name=reg_name,
            phone_number=reg_phone,
            telegram_id=message.from_user.id,
            telegram_username=f"@{telegram_username}"
        )
        await state.clear()
    else:
        await bot.send_message(
            message.from_user.id,
            f"⚠️Вказан не вірний номер телефону.\n\n"
            f"📞Вкажіть свій номер у форматі: 0951112233"
        )


@sync_to_async
def create_user(first_name, phone_number, telegram_id, telegram_username):
    Client.objects.create(
        first_name=first_name,
        phone_number=phone_number,
        telegram_id=telegram_id,
        telegram_username=telegram_username
    )
