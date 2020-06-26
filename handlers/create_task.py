from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db, bot
from states import CreateTask


# /add - wait for task description
@dp.message_handler(commands='task', state='*')
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
        
        # Get statuses
        statuses = db.get_statuses()
        print(statuses)
        # Send messages to all users
        users = db.get_users()
        for user in users:
            await bot.send_message(user[0],
                f'👀 Тew task "{task}" just has been added by @{username}')
    else:
        await message.answer(f'❌ Task "{task}" wasn`t created')
    await state.finish()