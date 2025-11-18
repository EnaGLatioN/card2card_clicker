import requests
import datetime

# Параметры запроса
params = {
    'traderId': '22314268-b9f0-48fd-8901-30419acd2419',
    'from': '2025-10-31T19:00:00.000Z',
    'to': '2025-11-18T13:19:39.884Z',
    'limit': 100,
    'offset': 0
}

url = 'https://api.cards2cards.com/v2/dashboard/trader/orders'

# Заголовки из вашего браузера (замените на актуальные значения)
headers = {
    'authority': 'api.cards2cards.com',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'ru,en;q=0.9',
    'authorization': 'AWS4-HMAC-SHA256 Credential=ASIAWU4LY6NXVLPE3KLW/20251118/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=a4402a009155a8cbf631d643e958e80b48eb70e2ae098bb693bc990ed2423464',
    'origin': 'https://dashboard.cards2cards.com',
    'priority': 'u=1, i',
    'referer': 'https://dashboard.cards2cards.com/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "YaBrowser";v="25.8", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 YaBrowser/25.8.0.0 Safari/537.36',
    'x-amz-date': '20251118T131942Z',
    'x-amz-security-token': 'IQoJb3JpZ2luX2VjEP7//////////wEaCXVzLWVhc3QtMSJHMEUCIQDQMkNNmX7YW27zqRxPJdSlPDc+2bXsUu8Q+ie+/41NyAIgUR4UmZ5NBZCkY9zW7+V3lH2eWCeEglwIWTobcwQzx/oqzwQIxv//////////ARADGgw0NTcxNzAyODU0MjMiDMNR6Y43LefNTato5iqjBOPfqBLG5EbdKAESYpgn360WQ05zMVrLYRF3n3N8/qy+vWEwMm1EuEypBXJB4gKzeBfh6HFcJ3hbIQ0rNVojDyFr4yTpILKCQvqzWGHDDw0r6uFRdKMG9ARu9lZ8y1QWaIMiedk5avaSSmT7fIkK9YkpOaTMCje6+DBKgI05vxrebyIvHaNm4z0TUcsDtd6sJ3Sir87xyIANi6n1rSEy3nWHOKwZEb5yi8HmpjOzO/z1goOQL0t9iNVd+U5cOUk2MzprCMDYQNlwVz/m01svDUpJm6+5+St7CH8QSANSoCAKR3PwVqHM4uBcFbjy/YQXvYHMgWJ1/UVmyzjE34+ZqvUB6HfKIqUEFd6IFOMLt7vKUwS84nck05h5etOesCb6Wn/Kz/oRG7nnsmhMQZt1NmUxaKpwK1/o7V9/POb3fS56Vec9/2rXSVRrIweX5XCPsD0WTEld6ZwZSWb7e11BJWT/4Bq/g4s+gf8NPqnVbXFeznMr8S1M7VjpeeFT5xW63sFw0G5D4fwxQK8t09wtiKIJIuibo8MSSt7UvGNj1sWMb0GOGlJRWV28V7kmXfabrMTZubRdfDlUUXZBuVUFiwUjYwcl1vNXbtxxT0ZDvUktuz1PphMxns+3WLhJrTuvjf2P7fD7d7P8f9dPsb2IAmYSP78NAi4jhXxme5UT4XljgnqvY/mQ0ru2gGiN72AFFDcj/qsj5c0Awr2DlBFILTTnpSgwxuTxyAY6gwKQkLR7qLedFdrCgyoaAmHwFmLmnYQnw+8EUPoPC7ghY6DjNnwsKeqvM5qQcdWmm7nOwE/ydOU6AV06AJQWxTs2pQTRrwVNbwdQFPFkw80PlIn/D/y2Qv67/I+azmo94liBaPojAz8pqwFFHfug01iAG1FSyjHAffe+hkbQHMqeXZeSkAoXZfPFLhu5IhWI1Q2EfnW1FW/o3H4ME1dyHuW8VpEm4G9+iW09qFKdB2velNw2PvN9a/ll4R9BGxAI8U+bsz/rj0edWnG9q3aVMKZvMZlECxNTVA5yVfnjK8Ny3WdwQ64tfNPxfjDD73v9+ViXLNXp9snfXoiJIkmvi7wJmZyY'
}

try:
    response = requests.get(url, params=params, headers=headers)

    print(f"Статус код: {response.status_code}")
    print(f"URL запроса: {response.url}")

    if response.status_code == 200:
        print("УСПЕХ! Данные получены:")
        print(response.json())
    else:
        print(f"Ошибка: {response.status_code}")
        print(f"Текст ответа: {response.text}")

except Exception as e:
    print(f"Ошибка при выполнении запроса: {e}")