from aiogram.fsm.state import StatesGroup, State


class OrderState(StatesGroup):
    car = State()
    sales_department = State()
    confirm_description = State()
    description = State()
