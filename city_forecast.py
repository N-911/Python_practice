import sys
import pprint
import requests
from dateutil.parser import parse


# import unirest


class YahooWeatherForecast:

    def __init__(self):
       self._city_cache = {}

    def get(self, city):
        # if city in self._cached_data:
            # return self._cached_data[city]
        url = f"https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city}%22)%20and%20u%3D%27c%27&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        data = requests.get(url).json()
        forecast = []
        forecast_data = data["query"]["results"]["channel"]["item"]["forecast"]
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["date"]),
                "high_temp": int(day_data["high"])
            })
        # self._cached_data[city] = forecast
        return forecast


class CityInfo:

    def __init__(self, city, forecast_provider=None):
        self.city = city.lower()
        self._forecast_provider = forecast_provider or YahooWeatherForecast()

    def weather_forecast(self):
        return self._forecast_provider.get(self.city)

def _main():
    city_info = CityInfo('Kiev')
    # forecast = city_info.weather.forecast()
    # pprint.pprint(forecast)
    aa = YahooWeatherForecast.get('London')


if __name__ == "__main__":
    _main()
