from src.weather_execute import Weather


def main(city: str) -> None:
    """Стартовая точка проекта."""
    Weather().execute(city=city)


if __name__ == "__main__":
    current_city = str(input("Город: "))
    main(city=current_city)
