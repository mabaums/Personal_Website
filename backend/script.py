import json
import http.client


if __name__ == '__main__':
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "93e03c58cd2dcde693cc96a47ed67a71"
    }
    conn.request("GET", "/players?id=184&season=2021", headers=headers)
    data = json.loads(conn.getresponse().read())
    data = data['response'][0]
    f = open('data/players-39-2021/184.json', 'w')
    json.dump(data, f)
    print(data)