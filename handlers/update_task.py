from aiogram.types import CallbackQuery
from loader import dp, db
from helper import remove_special_symbols

import logging


@dp.callback_query_handler(text_contains='#')
async def process_callback_status(call: CallbackQuery):
    """ Метод обработки инлайн кнопок для изменения статуса задач """
    await call.answer(cache_time=60)
    callback_data = call.data.split(':')
    logging.info(f'call = {callback_data}')
    # Get status name
    status_id = remove_special_symbols(callback_data[1])
    status = db.get_status(status_id)[0][1]
    # Get task name
    task_id = callback_data[2]
    task = db.get_task(task_id)[0][1]
    # Telegram username of user pressed one of the btns
    username = callback_data[3] 
    # Ответ на нажатие Inline кнопки
    if db.update_status(task_id, status_id):
        await call.message.answer(f'@{username} установил статус "{status}"" для задачи "{task}"')
    


'''
@dp.message_handler(Command('update'), state='*')
async def update_task_step_1(message: Message):
    user_id = message.chat.id
    # If user exists and he is a customer
    if db.user_exists(user_id, 1):
        await message.answer('✔️ Доступ получен, права фармера')
        # Set name state, show kb with list of tasks
        await UpdateTask.select_task.set() 
        await message.answer('Выбери задачу',
            reply_markup=tasks_keyboard) 
    elif db.user_exists(user_id, 3):
        await message.answer('Авторизован как администратор')
    else:
        await message.answer('❌ Недостаточно прав')


# Process task select
@dp.message_handler(state=UpdateTask.select_task)
async def update_task_step_2(message: Message, state: FSMContext):
    task = message.text.split(' ')
    user_id = message.chat.id
    status_name = remove_special_symbols(task[3])
    task_id = remove_special_symbols(task[0])
    if db.task_exists(task_id):
        await UpdateTask.select_status.set() 
        await message.answer(f'Выбери статус', reply_markup=statuses_keyboard(
            db.get_status_by_name(status_name)
        ))
    else:
        await message.answer('❌ Произошла ошибка, попробуй снова')


# Process status updating
@dp.message_handler(state=UpdateTask.select_status)
async def update_task_step_3(message: Message, state: FSMContext):
    status_name = message.text
    if db.status_exists_by_name(status_name):
        # Update status
        # db.update_status(task_id, status_id)
        pass
    else:
        await message.answer('❌ Произошла ошибка, попробуй снова')

    await state.finish()
'''


