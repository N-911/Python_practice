"""Show weather forecast in entered city"""

import pprint
import requests
from dateutil.parser import parse

class Openweather:
    def __init__(self):
       self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        # APIKEY = '4c0c8b76915ac5704252b3679ed8c4ed'
        APIKEY = "243b9e2d517625e2c665ef01d495d87e"
        # url = f"http://api.openweathermap.org/data/2.5/forecast?id=703448&APPID={APIKEY}"
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={APIKEY}"
        data = requests.get(url).json()
        forecast = []
        forecast_data = data["list"]
        for i in forecast_data:
            forecast.append({
                "date": parse(i["dt_txt"]),
                "high_temp": (i['main']['temp_max'] - 273)
            })
        self._city_cache[city] = forecast
        return forecast


class CityInfo:

    def __init__(self, city, forecast_provider=None):
        self.city = city
        self._forecast_provider = forecast_provider or Openweather()

    def weather_forecast(self):
        return self._forecast_provider.get(self.city)

    # def __print__(self):
    #     return  f"date  - {self.weather_forecast(self)[0]}, tem - {self.weather_forecast(self)[1]}.f2"


def _main():
    city = input("Input city: ", )
    city_info = CityInfo(city)
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast[1])
    # print(forecast)

if __name__ == "__main__":
    _main()
