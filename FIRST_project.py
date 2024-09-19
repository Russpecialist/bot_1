import requests
import time


API_URL = 'https://api.telegram.org/bot'
API_FOX_URL = 'https://randomfox.ca/floof/'
BOT_TOKEN = ''
ERROR_TEXT = 'Здесь должна была быть картинка с лисичкой :('

offset = -2
counter = 0
response: requests.Response
link: str


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            response = requests.get(API_FOX_URL)
            if response.status_code == 200:
                link = response.json()['image']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1