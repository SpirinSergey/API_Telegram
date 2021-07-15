import requests
import conf

# Аутентификация по почте, паролю и переданному токену капчи
headers = {'accept': 'text/plain', 'Content-Type': 'text/json'}
data = '{"login":"spirin1504@mail.ru","password":"Sobaka123","capcha":"yuetf3iuofgiu34yftyh23iuouoydfroi23qehcfdguy"}'
response_log = requests.post('https://front.kcash.ru/api/fo/Login/SignIn', headers=headers, data=data).text

# Разрывать свою текущую сессию
response_out = requests.post('https://front.kcash.ru/api/fo/Login/Logout', {'accept': '*/*'}).text

# Получение кошельков пользователя
response_wal = requests.get('https://front.kcash.ru/api/fo/Account/GetUserWallets', {'accept': 'text/plain'}).text

# ПОлучение ip адреса пользователя
response_ip = requests.get('https://front.kcash.ru/api/fo/Account/GetUserIpAddress', {'accept': 'text/plain'}).text


