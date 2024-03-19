from datetime import datetime
from typing import Tuple

import requests
from bs4 import BeautifulSoup
from requests import Response


class _WeatherCity:
    """Погода города. (Компонентный)"""
    @staticmethod
    def __get_user_agent() -> dict[str, str]:
        """Получить user agent для заголовка."""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0 (Edition Yx GX)"
        }
        return headers

    @staticmethod
    def __get_response(current_city: str, headers: dict[str, str]) -> Response:
        """Получить ответ."""
        response = requests.get(
            url=f"https://www.google.com/search?q=погода+в+{current_city}",
            headers=headers,
        )
        return response

    @staticmethod
    def __get_html(response: Response) -> BeautifulSoup:
        """Получить html-страничку."""
        soup = BeautifulSoup(markup=response.text, features="html.parser")
        return soup

    @staticmethod
    def __get_weather(soup: BeautifulSoup) -> str:
        """Получить погоду."""
        weather = soup.select("#wob_dc")[0].getText()
        return weather

    @staticmethod
    def __get_time(soup: BeautifulSoup) -> str:
        """Получить время."""
        time = soup.select("#wob_dts")[0].getText().split(" ")[1]
        return time

    @staticmethod
    def __get_date() -> str:
        """Получить текущую дату."""
        return datetime.now().strftime("%Y-%m-%d")

    def execute(self, city: str) -> tuple[str, str, str, str]:
        """Выполнить получение информации о городе."""
        headers = self.__get_user_agent()
        response = self.__get_response(city, headers)
        soup = self.__get_html(response)
        weather = self.__get_weather(soup)
        time = self.__get_time(soup)
        date = self.__get_date()
        return city, time, date, weather
