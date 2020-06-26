from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db, bot
from states import CreateTask
from config import CHANNEL_ID

# /add - wait for task description
@dp.message_handler(Command('task'), state='*')
async def create_task_step_1(message: types.Message):
    user_id = message.chat.id
    await message.answer('✔️ Access is allowed')
    # If user exists and he is a customer
    if db.user_is_customer(user_id):
        # Set name state
        await CreateTask.name.set()
        await message.answer('Enter task description')   
    else:
        await message.answer('❌ You are not a customer')


# Process task description
@dp.message_handler(state=CreateTask.name)
async def create_task_step_2(message: types.Message, state: FSMContext):
    task = message.text
    user_id = message.chat.id
    username = message.chat.username
    if db.add_task(task, user_id):
        await message.answer(f'✔️ Task "{task}" was created')

        # Send message to TG channel
        await bot.send_message(CHANNEL_ID,
            f'👀 New task "{task}" just has been added by @{username}',
            reply_markup=statuses_keyboard)
    else:
        await message.answer(f'❌ Task "{task}" wasn`t created')
    await state.finish()