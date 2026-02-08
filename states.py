from aiogram.fsm.state import State, StatesGroup


class ConsultationFSM(StatesGroup):
    name = State()
    phone = State()
    date = State()
    time = State()
    format = State()
