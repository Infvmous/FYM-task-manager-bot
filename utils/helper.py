import config
from loader import bot, db


async def notify_channel(text):
    await bot.send_message(config.CHANNEL_ID, text)