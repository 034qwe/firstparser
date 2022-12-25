from aiogram.utils import executor
from create_bot import dp
from hendlers import other, wiki,rework_text
from keyboards import lang_kb

async def on_startup(_):
    print('bot start')


other.register_handlers_other(dp)
wiki.register_handlers_maintext(dp)
lang_kb.register_handlers_langkb(dp)
rework_text.register_handlers_rework(dp)


executor.start_polling(dp, skip_updates=True,on_startup=on_startup)