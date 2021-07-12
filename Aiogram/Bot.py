import logging
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
from conf import API_TOKEN
import API_koshelek_ru as ksl

# Настроить ведение журнала
logging.basicConfig(level=logging.INFO)

# Инициализировать бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'ХОЛОУ', reply_markup=kb.start_kb)


@dp.message_handler(commands=['Регистрация'])
async def send_welcome(message: types.Message):
    await message.reply(ksl.ip_koshelec)


@dp.message_handler(commands=['Войти'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, ksl.ip_koshelec)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
