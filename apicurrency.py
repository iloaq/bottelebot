import requests


def currency_data1(currency):
    data = requests.get(f'https://api.exchangerate.host/latest?base=USD').json()
    return round(data['rates'][currency],2)

