from aiogram.fsm.state import StatesGroup, State


class ChangeUserPhone(StatesGroup):
    phone_number = State()
