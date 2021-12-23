import requests
from yadisk import YaUploader
import time
from pprint import pprint


def get_hero_int(*args):
    hero_list = args
    access_token = 2619421814940190
    hero_int = {}
    for name in hero_list:
        url = f'https://superheroapi.com/api/{access_token}/search/{name}'
        response = requests.get(url)
        response = response.json()
        intelligence = response['results'][0]['powerstats']['intelligence']
        hero_int.update({intelligence: name})
    smartest_hero = max(hero_int.keys())
    smartest_hero = hero_int[smartest_hero]
    return smartest_hero


def get_news():
    today = int(time.time())
    yesterday = today - 86400
    date = f'fromdate={yesterday}&todate={today}'
    order = 'desc'
    sort = 'activity'
    tagged = 'Python'
    site = 'stackoverflow'
    url = f'https://api.stackexchange.com/2.3/questions?{date}&order={order}&sort={sort}&tagged={tagged}&site={site}'
    response = requests.get(url=url)
    response = response.json()
    return response


pprint(get_news())
print(get_hero_int('Thanos', 'Hulk', 'Captain America'))
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
