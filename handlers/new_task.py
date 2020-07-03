import config

from loader import dp, db
from utils.states import NewTask

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.reply.task_types import task_types


@dp.message_handler(Command('task'), state='*')
async def cmd_task(message: Message):
    user_id = message.from_user.id
    user = db.get_where(config.USERS_TABLE, user_id)
    user_group = user[3] if user is not None else None
    if user_group == 2 or 3:
        await NewTask.select_type.set()
        await message.answer('Выбери тип задачи',
            reply_markup=await task_types())
    else:
        await message.answer('❌ Недостаточно прав')


@dp.message_handler(state=NewTask.select_type)
async def cmd_task_select_type(message: Message, state: FSMContext):
    task_type = message.text
    task_types = db.get_all(config.TYPES_TABLE)
    if any(task_type in i for i in task_types):
        await NewTask.name.set()
        print('SAY')
    else:
        await message.answer('❌ Выбери из клавиатуры')