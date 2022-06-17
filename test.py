from woocommerce import API
import apicurrency

wcapi = API(
    url="https://mining4-you.com/",
    consumer_key="ck_c108305d724ec87d49c07bff46debc5356e493ef",
    consumer_secret="cs_293377acb30b49b0e7917c77617fa798859b13a6",
)

datacost = wcapi.get(f'products?slug=antminer-s19xp').json()
cost = datacost[0]

print(cost)