import requests

response = requests.get('http://api.open-notify.org/astros.json')
data = response.json()

print(response.status_code)

people = data['people']
for person in people[:5]:
  print(person['name'])