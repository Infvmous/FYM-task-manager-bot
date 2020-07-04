from aiogram.types import CallbackQuery

from loader import dp, db, bot
from config import CHANNEL_ID, STATUS_ROW, TASKS_TABLE

import logging


add_on = '#'


@dp.callback_query_handler(text_contains=add_on)
async def process_callback_status(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data.split(':') # get callback to tuple
    logging.info(f'call = {callback_data}') # log callback
    # Get status name by id from the callback
    status_id = callback_data[1].replace(add_on, '')
    task_id = callback_data[2]
    if db.update(TASKS_TABLE, status_id, STATUS_ROW, task_id):
        await call.message.answer(f'✅ Для задачи {task_id} установлен статус {status_id}')
    else:
        await call.message.answer('❌ При изменении статуса произошла ошибка')




