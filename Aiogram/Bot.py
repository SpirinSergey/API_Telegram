from aiogram import Bot, Dispatcher, executor, types
from conf import API_TOKEN, token_kap
import koshelek_api as ks
import keyboards as kb
import logging

# Настроить ведение журнала
logging.basicConfig(level=logging.INFO)

# Инициализировать бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите действие:', reply_markup=kb.start_kb)


@dp.message_handler(commands=['ip_address'])
async def send_welcome(message: types.Message):
    await message.reply(ks.ip_address)


@dp.message_handler(commands=['Войти'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'в разработке...')


@dp.message_handler(commands=['Регистрация'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'в разработке...')


@dp.message_handler(commands=['Обновить'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'в разработке...')


@dp.message_handler(commands=['Смена пароля'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'в разработке...')


@dp.message_handler(commands=['Выйти'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'в разработке...')


@dp.message_handler(commands=['Выгнать'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'в разработке...')


@dp.message_handler(commands=['2 факт. аутент.'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'в разработке...')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
