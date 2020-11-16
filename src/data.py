import requests


def download_data():
    url = 'https://www.metaweather.com/api/location/44418/2020/11/13/'
    response = requests.get(url)

    # make sure the request was successful
    response.raise_for_status()

    return response.json()
