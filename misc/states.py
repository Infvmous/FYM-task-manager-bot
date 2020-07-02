from aiogram.dispatcher.filters.state import State, StatesGroup


class AddTask(StatesGroup):
    # Add steps for task creation
    name = State()

class AddUser(StatesGroup):
    user_info = State()