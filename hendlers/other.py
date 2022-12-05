from create_bot import dp,bot 
from aiogram import types,Dispatcher


async def hello_send(message:types.Message):
    await message.answer(f'Hello {message.from_user.first_name}')


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(hello_send,commands=['start'])