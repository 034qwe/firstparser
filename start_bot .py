from aiogram.utils import executor
from create_bot import dp
from hendlers import maintext, other
from keyboards import lang_kb

async def on_startup(_):
    print('bot start')

other.register_handlers_other(dp)
maintext.register_handlers_maintext(dp)
lang_kb.register_handlers_langkb(dp)

executor.start_polling(dp, skip_updates=True,on_startup=on_startup)