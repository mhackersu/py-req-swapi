import requests
req = requests.get('https://swapi.dev/api/planets/')
print(req.text)
