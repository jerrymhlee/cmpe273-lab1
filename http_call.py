import requests

for i in range(0,3):
    r = requests.get('https://webhook.site/81c75d7d-f9c7-48f6-ab55-b59b5c410e02')
    print(r.headers['Date'])

