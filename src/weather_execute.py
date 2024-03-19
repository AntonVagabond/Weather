from src.weather_city import _WeatherCity
from src.weather_write import _WeatherWrite


class Weather:
    """Класс погоды. (Составной)"""
    def __init__(self):
        self.__weather_city = _WeatherCity
        self.__weather_write = _WeatherWrite

    def execute(self, city):
        """Выполнить действия проекта."""
        data: tuple[str, str, str, str] = self.__weather_city().execute(city=city)
        self.__weather_write(data).execute()
