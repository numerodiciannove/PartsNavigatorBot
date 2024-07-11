from aiogram.fsm.state import StatesGroup, State


class RegisterVinCode(StatesGroup):
    vin_code = State()


class DeleteVinCode(StatesGroup):
    vin_code = State()
