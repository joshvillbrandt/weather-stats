from src.data import download_data
from src.processing import process_data

data = download_data(hostname='https://www.metaweather.com')
output = process_data(data=data)

print(output)
