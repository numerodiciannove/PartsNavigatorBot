from aiogram.fsm.state import StatesGroup, State


class ChangeUserName(StatesGroup):
    first_name = State()
