from config import CHANNEL_ID
from loader import bot
from keyboards.inline.status_buttons import statuses_keyboard


def remove_special_symbols(string):
    """ Remove special symbols from string """
    alphanumeric = [character for character in string if character.isalnum()]
    alphanumeric = ''.join(alphanumeric)
    return alphanumeric


async def send_message_to_telegram(task, username, task_id):
    """ Отправить сообщение если задача добавлена в базу данных """
    await bot.send_message(CHANNEL_ID,
        f'👀 Новая задача "{task}" была добавлена пользователем @{username}',
        reply_markup=await statuses_keyboard(task_id, username))