import re


class MockApi():
    def __init__(self, mocker, hostname):
        # routes
        location_data_url = re.compile(hostname + '/api/location/44418/2020/11/13/')
        mocker.get(location_data_url, json=self._get_location_data_url)

        # introspection
        self.last_request = None
        self.requests = []

    def _handle_disconnect(self):
        pass

    def _get_location_data_url(self, request, context):
        self._handle_disconnect()

        # introspection
        self.requests.append(request)

        data = [
            {
                "id": 6698027872944128,
                "weather_state_name": "Light Rain",
                "weather_state_abbr": "lr",
                "wind_direction_compass": "WSW",
                "created": "2020-11-13T21:20:03.562376Z",
                "applicable_date": "2020-11-13",
                "min_temp": 9.18,
                "max_temp": 13.215,
                "the_temp": 13.055,
                "wind_speed": 5.249664922489992,
                "wind_direction": 249.6847205583789,
                "air_pressure": 1011,
                "humidity": 73,
                "visibility": 8.568087369760597,
                "predictability": 75
            },
            {
                "id": 6395314350063616,
                "weather_state_name": "Light Rain",
                "weather_state_abbr": "lr",
                "wind_direction_compass": "WSW",
                "created": "2020-11-13T18:20:01.749758Z",
                "applicable_date": "2020-11-13",
                "min_temp": 9.44,
                "max_temp": 12.975000000000001,
                "the_temp": 12.7,
                "wind_speed": 5.560900241559956,
                "wind_direction": 250.69264487165236,
                "air_pressure": 1011.5,
                "humidity": 72,
                "visibility": 8.718148512685914,
                "predictability": 75
            },
        ]

        # generate response
        context.status_code = 200
        return data
