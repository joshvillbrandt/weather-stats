import requests


def download_data(hostname):
    url = f'{hostname}/api/location/44418/2020/11/13/'
    response = requests.get(url)

    # make sure the request was successful
    response.raise_for_status()

    return response.json()
