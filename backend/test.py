import http.client

import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "93e03c58cd2dcde693cc96a47ed67a71"
    }

conn.request("GET", "/fixtures?league=39&season=2021", headers=headers)

res = conn.getresponse()
data = res.read()

f = open('data/fixtures.json', 'w')
f.write(data.decode('utf-8'))
f.close()
print(data.decode("utf-8"))