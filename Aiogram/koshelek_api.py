import requests

# API koshelek.ru
ip_address = requests.get('https://front.kcash.ru/api/fo/Account/GetUserIpAddress').text
logout = requests.get('https://front.kcash.ru/api/fo/Login/Logout')