from aiogram.dispatcher.filters.state import State, StatesGroup


class AddTask(StatesGroup):
    name = State()


class AddUser(StatesGroup):
    user_info = State()