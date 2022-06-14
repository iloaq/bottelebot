import requests


def currency_data1(currency):
    data = requests.get(f'https://v6.exchangerate-api.com/v6/2337ed5b676ac17fd0d3b450/latest/USD').json()
    return round(data['conversion_rates'][currency],3)

