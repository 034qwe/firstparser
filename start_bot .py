from aiogram.utils import executor
from create_bot import dp
from hendlers import other, wiki
from keyboards import lang_kb
from selenium_folder import main_selenium


async def on_startup(_):
    print('bot start')


other.register_handlers_other(dp)
wiki.register_handlers_maintext(dp)
lang_kb.register_handlers_langkb(dp)
main_selenium.register_handlers_selenium(dp)


executor.start_polling(dp, skip_updates=True,on_startup=on_startup)