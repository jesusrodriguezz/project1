import requests
myobj = {'text': 'great'}
response = requests.post('http://text-processing.com/api/sentiment/', data = myobj)
print(response.json())
