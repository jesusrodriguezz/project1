import requests

CLIENT_ID = "ea022069252f42a18e566926f41203e2 "
CLIENT_SECRET = "ed287404068e4d948d552d0f1103912d"

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'

track_id = input('Enter track id: ')

song_url = 'https://open.spotify.com/album/5MS3MvWHJ3lOZPLiMxzOU6?si=mmEruIAdQ7G9uFpDP7dyvg'

song_id = song_url.split("/")[-1]

print(song_id)

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
print(r.json())

