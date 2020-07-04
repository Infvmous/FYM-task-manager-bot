import utils.helper as helper

from config import EXT_ID, GRP, USERS_TABLE, \
    TYPES_TABLE, NAME_ROW

from loader import dp, db
from utils.states import NewTask

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.reply.task_types import task_types


@dp.message_handler(Command('task'), state='*')
async def cmd_task(message: Message):
    user_id = message.from_user.id
    user = db.get(USERS_TABLE, user_id, GRP, EXT_ID)
    user_group = user[0] if user is not None else None
    if user_group == 2 or 3:
        await NewTask.select_type.set()
        await message.answer('Выбери тип задачи',
            reply_markup=await task_types())
    else:
        await message.answer('❌ Недостаточно прав')


@dp.message_handler(state=NewTask.select_type)
async def cmd_task_select_type(message: Message, state: FSMContext):
    task_type = message.text
    task_types = db.get_all(TYPES_TABLE)
    if any(task_type in i for i in task_types): # If user entered type from keyboard
        await NewTask.name.set()
        await state.update_data(task_type=task_type) # Collect task type
        await message.answer('Введи имя задачи')
    else:
        await message.answer('❌ Выбери из клавиатуры')


@dp.message_handler(state=NewTask.name)
async def cmd_task_enter_name(message: Message, state: FSMContext):
    task = message.text # task name
    data = (await state.get_data()).get('task_type') # get task type name from keyboard
    task_type = db.get(TYPES_TABLE, data, row=NAME_ROW)[0] # get task type id from db by name
    username = message.from_user.username
    tg_id = message.from_user.id # chat id
    user_id = db.get(USERS_TABLE, tg_id, row=EXT_ID)[0] # user id from db by telegram id
    date = await helper.current_datetime() # current date and time
    # Collect data for task
    task_added, task_id = db.add_task(task, user_id, date, task_type)
    if task_added:
        text = [
            f'🔔 НОВАЯ ЗАДАЧА: {data}\n',
            f'📌 {task}',
            f'от @{username}'
        ]
        await message.answer(f'✅ Задача "{task}" успешно создана')
        await helper.notify_channel('\n'.join(text)) # Send message to channel
        await helper.notify_users('\n'.join(text), task_id) # Send message to all users
    else:
        await message.answer(f'❌ Задача "{task}" не была добавлена')
    await state.finish()