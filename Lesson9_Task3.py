from datetime import timedelta, datetime
import time
import requests
from pprint import pprint

def convert_day_now():
    now_day = datetime.now()
    # Определяем дату на данный момент, и переводим её в формат unix для последущей передачи в параметры поиска запроса
    stime = now_day.strftime('%Y-%m-%d')
    now_day = datetime.strptime(stime, "%Y-%m-%d").timestamp()
    return int(now_day)
def convert_two_day_ago():
    now_day = datetime.now()
    two_day = timedelta(days=2)
    two_days_ago = now_day - two_day
    # now_day - 2 day для поиска за два дня. Переводим в unix
    stime = two_days_ago.strftime('%Y-%m-%d')
    two_days_ago = datetime.strptime(stime, "%Y-%m-%d").timestamp()
    return int(two_days_ago)


def questions_python():
    url = 'https://api.stackexchange.com/2.2/questions'
    params = {'order': 'desc', 'sort': 'creation', 'tagged': 'python', 'site': 'stackoverflow',
              'fromdate': convert_two_day_ago(), 'todate': convert_day_now()}
    answer = requests.get(url, params=params).json()

    for link in answer['items']:
        print(link['title'])
        print(link['link'])
        print()

questions_python()