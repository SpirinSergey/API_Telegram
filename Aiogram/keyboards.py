from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# кнопки
btn_reg = KeyboardButton('Регистрация')
btn_in = KeyboardButton('Войти')
btn_ref = KeyboardButton('Обновить')
btn_pwd = KeyboardButton('Смена пароля')
btn_2fa = KeyboardButton('2 факт. аутент.')
btn_out = KeyboardButton('Выйти')
btn_out_all = KeyboardButton('Выгнать')
btn_my_ip = KeyboardButton('ip_address')

# КЛАВИАТУРЫ:
# -клавиатура старта
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    btn_reg).add(btn_in).add(btn_my_ip)

# -клавиатура после аутентификации
log_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    btn_ref, btn_2fa, btn_pwd, btn_out)
