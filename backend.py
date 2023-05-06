import requests
# from config import API_KEY
import os


def get_data(place, forecast_days):
    # if API_KEY:
        # url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    # else:
    API_KEY_ENV = os.environ["API_KEY"]
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY_ENV}"

    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))