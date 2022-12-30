from create_bot import dp,bot 
from aiogram import types,Dispatcher
from keyboards.lang_kb import change_kb

async def hello_send(message:types.Message):
    await message.answer(f'Hello {message.from_user.first_name}\nthe /rework command may take some time')

async def change_lang(message: types.Message):
    await message.answer('select your language',reply_markup=change_kb)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(hello_send,commands=['start'])
    dp.register_message_handler(change_lang,commands=['remove_lang'])