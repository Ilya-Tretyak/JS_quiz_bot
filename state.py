from aiogram.fsm.state import State, StatesGroup


class StatusTest(StatesGroup):
    choose_level = State()
    q_1 = State()
    q_2 = State()
    q_3 = State()
    q_4 = State()
    q_5 = State()
    q_6 = State()
    q_7 = State()