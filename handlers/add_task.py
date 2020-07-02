from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db, bot

from misc.states import AddTask
from misc.helper import send_message_to_telegram


# /add - wait for task description
@dp.message_handler(Command('add'), state='*')
async def add_task_step_1(message: Message):
    user_id = message.chat.id
    # If user exists and he is customer or admin
    if db.user_exists(user_id, 2) or db.user_exists(user_id, 3):
        await message.answer('✔️ Доступ получен')
        # Set name state
        await AddTask.name.set()
        await message.answer('Введи описание задачи')   
    elif db.user_exists(user_id, 3):
        await message.answer('Авторизован как администратор')
    else:
        await message.answer('❌ Недостаточно прав')


# Process task description
@dp.message_handler(state=AddTask.name)
async def add_task_step_2(message: Message, state: FSMContext):
    task = message.text
    user_id = message.chat.id
    username = message.chat.username
    # Collect task id and if task added send msg
    task_added, task_id = db.add_task(task, user_id)
    if task_added:
        msg = f'👀 Новая задача "{task}" была добавлена пользователем @{username}'
        await message.answer(f'✔️ Задача "{task}" успешно создана')
        await send_message_to_telegram(msg, task_id) # Send message to TG channel
        await send_message_to_telegram(msg, task_id, False) # Send to all users
    else:
        await message.answer(f'❌ Задача "{task}" не была создана')
    await state.finish()