from aiogram.fsm.state import StatesGroup, State


class RegisterState(StatesGroup):
    first_name = State()
    phone_number = State()
