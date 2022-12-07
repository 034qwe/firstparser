from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram import types,Dispatcher
from create_bot  import dp,bot 

language = 'uk'

change_kb= InlineKeyboardMarkup(row_width=3)

butt1 = InlineKeyboardButton(text='uk',callback_data='change_uk')
butt2 = InlineKeyboardButton(text='en',callback_data='change_en')
butt3 = InlineKeyboardButton(text='ru',callback_data='change_ru')

change_kb.row(butt1,butt2,butt3)


async def remove_en(massage:types.CallbackQuery):
    global language
    language = 'en'

def register_handlers_langkb(dp:Dispatcher):
    dp.register_callback_query_handler(remove_en,callback='change_en')