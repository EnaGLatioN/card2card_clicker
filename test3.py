import requests
import re


def search_js_files():
    # Получаем основную страницу
    main_response = requests.get('https://dashboard.cards2cards.com')
    main_html = main_response.text

    # Ищем ссылки на JS файлы
    js_pattern = r'src="([^"]+\.js)"'
    js_files = re.findall(js_pattern, main_html)

    user_pool_ids = []

    for js_file in js_files:
        if not js_file.startswith('http'):
            js_file = 'https://dashboard.cards2cards.com' + js_file

        try:
            js_response = requests.get(js_file, timeout=5)
            js_content = js_response.text

            # Ищем User Pool ID в JS файле
            patterns = [
                r'us-east-1_[a-zA-Z0-9]{8,}',
                r'UserPoolId["\']?:\s*["\'](us-east-1_[a-zA-Z0-9]+)["\']',
                r'userPoolId["\']?:\s*["\'](us-east-1_[a-zA-Z0-9]+)["\']'
            ]

            for pattern in patterns:
                matches = re.findall(pattern, js_content)
                user_pool_ids.extend(matches)

        except Exception as e:
            continue

    unique_ids = list(set(user_pool_ids))

    if unique_ids:
        print("Найдены в JS файлах:")
        for uid in unique_ids:
            print(f"  - {uid}")
    else:
        print("Не найдено в JS файлах")

    return unique_ids


search_js_files()