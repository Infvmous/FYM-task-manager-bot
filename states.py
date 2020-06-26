from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateTask(StatesGroup):
    # Add steps for task creation
    name = State()