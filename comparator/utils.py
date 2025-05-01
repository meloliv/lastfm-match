import requests
from dotenv import load_dotenv
import os

load_dotenv() 

API_KEY = os.getenv('LASTFM_API_KEY')

def get_top_artists(username):
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={username}&api_key={API_KEY}&format=json'
    response = requests.get(url)

    data = response.json()
    artists = []

    for item in data.get('topartists', {}).get('artist', []):
        artists.append(item['name'])

    return artists
