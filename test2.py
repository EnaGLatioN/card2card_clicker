import requests
import json

url = 'https://cognito-idp.us-east-1.amazonaws.com/'

payload = {
    "AuthFlow": "USER_PASSWORD_AUTH",
    "ClientId": "6eio0hlq4tmr2o9d30ht9cvfn7",
    "AuthParameters": {
        "USERNAME": "skotradde@gmail.com",
        "PASSWORD": "Helloworld1337!!!!!!!!"
    }
}

headers = {
    'Content-Type': 'application/x-amz-json-1.1',
    'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth'
}

try:
    print("Отправляем запрос аутентификации...")
    response = requests.post(url, json=payload, headers=headers)

    print(f"Статус код: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print("✅ Успешная аутентификация!")
        print(f"Access Token: {data['AuthenticationResult']['AccessToken'][:50]}...")
    else:
        print("Ответ сервера:")
        print(json.dumps(response.json(), indent=2))

except Exception as e:
    print(f"Ошибка: {e}")