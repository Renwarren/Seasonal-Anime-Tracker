import requests

def get_trending_anime():

    url = "https://kitsu.io/api/edge/trending/anime"

    response = requests.get(url)
    if response.status_code == 200:

        data = response.json()

        trending_anime = data['data']

        return trending_anime


def get_current_anime():
    url = 'https://kitsu.io/api/edge/anime'
    params = {
            'filter[status]': 'current',   
            'page[limit]': 4,  
        }

    response = requests.get(url, params=params)


    if response.status_code == 200:
        data = response.json()

        anime = data['data']
        return anime

def get_upcoming_anime():
    url = 'https://kitsu.io/api/edge/anime'
    params = {
        'filter[status]': 'upcoming',   
        'page[limit]': 4,  
    }

    response = requests.get(url, params=params)


    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the list of anime
        upcoming_anime = data['data']
        return upcoming_anime


