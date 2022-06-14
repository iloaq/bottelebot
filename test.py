import requests

url = "https://api-prod.poolin.com/api/public/v2/platform/cloud/{puid}/transfer"

payload={'coin_type': 'eth',
'unit': 'M',
'hashrate': '1',
'to': 'laxxe',
'start_time': '1635566400',
'end_time': '1636689600'}
files=[

]
headers = {
  'authorization': 'Bearer poolOt4dpKTUMiyIgGw0MihfQ9*************************04PeuppZyOaTC'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)