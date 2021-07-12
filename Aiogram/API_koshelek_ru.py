import requests

# API koshelek.ru
ip_koshelec = requests.get('https://front.kcash.ru/api/fo/Account/GetUserIpAddress').text
