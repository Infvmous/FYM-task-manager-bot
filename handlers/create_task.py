from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from misc import dp, db


class CreateTask(StatesGroup):
    # Add steps
    name = State()


# /add - wait for task description
@dp.message_handler(commands='add', state='*')
async def create_task_step_1(message: types.Message):
    user_id = message.chat.id
    await message.answer('Your telegram id is ' + str(user_id))
    
    if db.customer_exists(user_id):
        # Set name state
        await CreateTask.name.set()
        await message.answer('Enter task description')   
    else:
        await message.answer('You`re not a customer')


# Process task description
@dp.message_handler(state=CreateTask.name)
async def create_task_step_2(message: types.Message, state: FSMContext):
    task_description = message.text
    user_id = message.chat.id
    if db.create_task(task_description, user_id):
        await message.answer(f'Task "{task_description}" was created\nCustomer {user_id}')
    else:
        await message.answer(f'Task "{task_description}" wasn`t created')
    await state.finish()