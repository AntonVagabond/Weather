from functools import singledispatchmethod


class _WeatherWrite:
    """Запись погоды. (Компонентный)"""
    @singledispatchmethod
    def __init__(self, city: str, time: str, date: str, weather: str) -> None:
        self.__city = city
        self.__time = time
        self.__date = date
        self.__weather = weather

    @__init__.register(tuple)
    def __from_tuple(self, data: tuple[str, str, str, str]) -> None:
        self.__city, self.__time, self.__date, self.__weather = data

    def __output_to_terminal(self) -> None:
        """Вывод на терминал."""
        print(f"{self.__city}_{self.__date} {self.__time}_{self.__weather}")

    def __write_data_to_file(self) -> None:
        """Записать данные в файл."""
        with open("logs.txt", "w", encoding="utf-8") as file:
            file.write(f"{self.__city}_{self.__date} {self.__time}_{self.__weather}")

    def execute(self) -> None:
        """Выполнить вывод на терминал и запись данных в файл."""
        self.__output_to_terminal()
        self.__write_data_to_file()
