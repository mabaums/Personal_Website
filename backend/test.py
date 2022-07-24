import http.client
import json
import http.client
import time

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "93e03c58cd2dcde693cc96a47ed67a71"
    }


if __name__ == '__main__':
    f = open('data/fixtures.json')
    j_f = json.load(f)
    f.close()
    fixtures = j_f['response']
    for fixture in fixtures:
        time.sleep(0.5)
        conn.request("GET", "/fixtures/players?fixture={}".format(fixture['fixture']['id']), headers=headers)
        res = conn.getresponse()
        data = res.read()
        f = open('data/fixtures-39-2021/{}.json'.format(fixture['fixture']['id']), 'w')
        f.write(data.decode('utf-8'))
        f.close()
        print(data.decode("utf-8"))