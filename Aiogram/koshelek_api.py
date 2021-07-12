import requests

# API koshelek.ru
ip_address = requests.get('https://front.kcash.ru/api/fo/Account/GetUserIpAddress').text
