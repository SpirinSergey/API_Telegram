import requests
from config import token_capcha, login, password, url
from fake_useragent import UserAgent

ua = UserAgent().random
sess = requests.Session()


# Аутентификация по почте, паролю и переданному токену капчи
def sign_in():
    headers = {
        'User-agent': ua,
        'accept': 'text/plain',
        'Content-Type': 'text/json',
    }
    data = '{"login":' + login + ',"password":' + password + ',"capcha":' + token_capcha + '}'
    return sess.post(url + '/api/fo/Login/SignIn', headers=headers, data=data).text


# обновление access токена
def refresh_token():
    headers = {
        'User-agent': ua,
        'accept': 'text/plain',
    }
    params = (
        ('ResfreshToken', 'lKqWHUCCnEcolKlDGnnm8Dzxd95ugto5dLkoroWDpo0'),
        ('RefreshToken', 'i9rRJ5VcGAcSYs9fCkwEWgAYW508ykIS1SypBE7tgo4'),
    )
    return sess.put(url + '/api/fo/Login/RefreshToken', headers=headers, params=params).text


# Разрывать свою текущую сессию
def logout():
    headers = {
        'User-agent': ua,
        'accept': '*/*',
    }
    return sess.post(url + '/api/fo/Login/Logout', headers=headers).text


# Получение кошельков пользователя
def get_user_wallets():
    headers = {
        'accept': 'text/plain',
    }
    return requests.get(url + '/api/fo/Account/GetUserWallets', headers=headers).text


# Получение ip адреса пользователя
def get_user_ip_address():
    headers = {
        'accept': 'text/plain',
    }
    return requests.get(url + '/api/fo/Account/GetUserIpAddress', headers=headers).text
