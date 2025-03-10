from http import HTTPStatus

import requests



class Weather:
    """Creates a Weather object getting an apikey as input and lat and lon coordinates.

    ## Package use example:

    - create a weather object using an apikey, coordinates and units (optionally)
    - you can use units: standard, metric and imperial, default to `metric`
    - the apikey below is not guaranteed to work.
    - get your own apikey from https://openweathermap.org/
    - and wait a couple of hours for the apikey to be activated

    >>> weather1 = Weather(apikey="r242redsfwdwdd", lat=22.1, lon=42.2)

    ### Get complete weather data for the next 12 hours:
    >>> weather1.next_12h()

    ### Get simplified data for the next 12 hours:
    >>> weather1.next_12h_simplified()

    """
    base_url = (
        "https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}"
    )
    def __init__(self, api_key: str, lat: float, lon: float, units: str = "metric"):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.units = units
        self.url = self.__build_url()

        self.data = self.__get_data()

    def __build_url(self) -> str:
        return self.base_url.format(
            lat=self.lat, lon=self.lon, units=self.units, api_key=self.api_key
        )

    def __get_data(self) -> dict:
        response = requests.get(self.url)
        response_json = response.json()

        if int(response_json["cod"]) != HTTPStatus.OK:
            raise ValueError(response_json["message"])

        return response_json

    def next_12h(self) -> list:
        """Returns 3-hours data for the next 12 hours as a list.
        """
        return self.data["list"][:4]

    def next_12h_simplified(self) -> list:
        """Returns date, minimum temperature, temperature expected, maximum temperatura and 
        sky condition every 3 hours for the next 12 hours as a list of tuples.
        """
        simplified_data = list()

        for hour_data in self.data["list"][:4]:
            simplified_data.append(
                (
                    hour_data["dt_txt"],
                    hour_data["main"]["temp_min"],
                    hour_data["main"]["temp"],
                    hour_data["main"]["temp_max"],
                    hour_data["weather"][0]["description"]
                )
            )
        return simplified_data
