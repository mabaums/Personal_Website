import json

if __name__ == '__main__':
    f = open('data/39-2021.json', encoding='utf-8')
    data = json.load(f)
    data = data['response'][0]['league']['standings'][0]

    id_dict = {}
    for d in data:
        id_dict[d['team']['name']] = d['team']['id']
    print(id_dict)
    f.close()