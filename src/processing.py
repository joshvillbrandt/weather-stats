def process_data(data):
    temp_sum = 0

    for measurement in data:
        temp_sum += measurement['the_temp']

    average = temp_sum / len(data)

    return average
