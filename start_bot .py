from aiogram.utils import executor
from create_bot import dp
from hendlers import maintext, other


async def on_startup(_):
    print('bot start')

other.register_handlers_other(dp)
maintext.register_handlers_maintext(dp)


executor.start_polling(dp, skip_updates=True,on_startup=on_startup)