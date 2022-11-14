import requests

heroes_listed = ['Hulk', 'Captain America', 'Thanos']


def find_smartest(heroes_listed):
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    resp = requests.get(url + "/all.json").json()
    name_n_itel = {}
    for names in resp:
        if names['name'] in heroes_listed:
            name = names["name"]
            intel = names["powerstats"]["intelligence"]
            name_n_itel[name] = intel
    some_sort = sorted(name_n_itel.items(), reverse=True)
    print(f'Самый умный: {some_sort[0][0]}, Интеллект: {some_sort[0][1]}')


find_smartest(heroes_listed)