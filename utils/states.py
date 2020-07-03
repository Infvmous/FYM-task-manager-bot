from aiogram.dispatcher.filters.state import State, StatesGroup


class NewTask(StatesGroup):
    select_type = State()
    name = State()


class NewUser(StatesGroup):
    data = State()
    select_group = State()