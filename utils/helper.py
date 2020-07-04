import config as cfg

from datetime import datetime
from loader import bot, db
from keyboards.inline.task_statuses import statuses_keyboard


async def notify_channel(text):
    await bot.send_message(cfg.CHANNEL_ID, text)


async def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


async def notify_users(text, task_id = None):
    users = db.get_users(3)
    for user in users:
        if task_id is not None:
            await bot.send_message(user[1], text,
                reply_markup=await statuses_keyboard(task_id))
        else:
            await bot.send_message(user[1], text)

