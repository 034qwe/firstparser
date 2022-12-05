from aiogram import Bot 
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5435074897:AAGSirW4rC5seTYFjxk0m_t6yosCS9bHB1Y'

bot = Bot(token=TOKEN)
dp =Dispatcher(bot,storage=MemoryStorage())