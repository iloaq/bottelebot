from woocommerce import API
import apicurrency

wcapi = API(
    url="https://mining4-you.com/",
    consumer_key="ck_c108305d724ec87d49c07bff46debc5356e493ef",
    consumer_secret="cs_293377acb30b49b0e7917c77617fa798859b13a6",
)


calcin="0"

def api_minerinfo(calcin):
    minerinfo = wcapi.get(f'products?slug={calcin}').json()
    return minerinfo[0]['name']

def api_miners(calcin):

    prods = wcapi.get(f'products?slug={calcin}').json()
    try:
        prods = prods[0]['slug']
    except IndexError:
        prods = '0'

    return prods

def api_minerenergy(calcin):
    minerenergy = wcapi.get(f'products?slug={calcin}').json()
    return minerenergy[0]['attributes'][1]['options'][0]

def api_minerth(calcin):
    minerth = wcapi.get(f'products?slug={calcin}').json()
    return minerth[0]['attributes'][0]['options'][0]

def api_minercost(calcin):
    datacost = wcapi.get(f'products?slug={calcin}').json()
    cost = float(datacost[0]['price'])
    cur = float(apicurrency.currency_data1('RUB'))
    minercost = float(cost / cur)
    return minercost


