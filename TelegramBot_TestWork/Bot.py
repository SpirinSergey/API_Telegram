from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
import convert_curl as cc
import keyboards as kb
import logging

# Настроить ведение журнала
logging.basicConfig(level=logging.INFO)

# Инициализировать бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Создание списка входящих команд
command_bot = ['Регистрация', 'Войти', 'Обновить', 'Смена пароля', '2 факт. аутент.', 'Выйти', 'Выгнать', 'ip_address']

# Создание словаря
dict_btn = {'Регистрация': 'в разработке...', 'Войти': cc.sign_in(), 'Обновить': cc.get_user_wallets(),
            'Смена пароля': 'в разработке...', '2 факт. аутент.': 'в разработке...', 'Выйти': cc.logout(),
            'Выгнать': 'в разработке...', 'ip_address': cc.get_user_ip_address()}


# @dp.callback_query_handler(func=lambda c: c.data == 'button1')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите действие:', reply_markup=kb.start_kb)


@dp.message_handler(lambda message: message.text in command_bot)
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, dict_btn[message.text], reply_markup=kb.log_kb)



# bot.py
@dp.message_handler(commands=['1'])
async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка", reply_markup=kb.inline_kb1)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
