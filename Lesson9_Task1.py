import requests
from pprint import pprint

token = '2619421814940190'
url_search = f'https://superheroapi.com/api/{token}/search/'

names = ['Hulk', 'Captain America', 'Thanos']
dict_name_intell = {}

for name in names:
    intel = int(requests.get(url_search + name).json()['results'][0]['powerstats']['intelligence'])
    added_hero = {name : intel}
    dict_name_intell.update(added_hero)
print(dict_name_intell)
print()

for key, val in dict_name_intell.items():
    if val == max(list(dict_name_intell.values())):
        print(f'Самый умный из героев, это: {key}, c интеллект {val}')
