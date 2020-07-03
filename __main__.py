from loader import bot, storage
from utils.helper import notify_channel


async def on_startup(dp):
    await notify_channel('📣 Бот запущен')


async def on_shutdown(dp):
    await notify_channel('❗️Бот выключился')
    await bot.close()
    await storage.close()


if __name__ == "__main__":
    import handlers
    from aiogram import executor
    from loader import dp
    
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown,
                            skip_updates=True)
