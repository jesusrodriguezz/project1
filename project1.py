import requests
import json


API_KEY = "AIzaSyAYP2C_aLg1ll-oYvwwdgaYjAJJVGNNMDM "

url = ' https://www.googleapis.com/youtube/v3'
response = requests.post(url)
print(response)
