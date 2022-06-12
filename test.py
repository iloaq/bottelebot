
# msg = bot.send_message(message.chat.id,f'{data}\n '
#                                              f'{words.time_get()}\n'
#                                              f'{dif} {apibtc.get_difficulty()}\n'
#                                              f'{block} {apibtc.get_rewards()} BTC\n'
#                                              f'\n'
#                                              f'{btcdohod} 0.00000461 BTC\n'
#                                              f'{wordcourse}\n'
#                                              f'1 BTC = {round(float(apibtc.api_btc()),2)} USD\n'
#                                              f'{coursetoday}\n'
#                                              f'1$ = {apicurrency.currency_data1(currency)} {currency}\n'
#                                              f'{minermdoel} \n {Minername} ({th})\n'
#                                              f'\n'
#                                              f'{paywords} - {pay} {currency}\n'
#                                              f'\n'
#                                              f'{paydohod}: {dohod} {currency}\n'
#                                              f'{payrashod}: {rashod} {currency}\n'
#                                              f'{payprib}: {cash} {currency}\n'
#                                              f'{payokup}: {okup}', reply_markup=calcmenu
#                                          )
#
#
#
# msg = bot.send_message(message.chat.id,f'*{paydohod}: {dohod} {currency}*💰\n'
#                                        f'*{payrashod}: {rashod} {currency}*💵\n'
#                                        f'{payprib}: {cash} {currency}\n'
#                                        f'{payokup}: {okup}\n'
#                                        '\n'
#                                        f'📆{data}\n '
#                                        f'{words.time_get()}\n'
#                                        f'{minermdoel} - *{Minername} ({th})*\n'
#                                        f'{paywords} - *{pay} {currency}*\n'
#                                        '\n'
#                                        f'{wordcourse} 1 BTC = {round(float(apibtc.api_btc()),2)} USD\n'
#                                        f'1$ = {apicurrency.currency_data1(currency)} {currency}\n'
#                                        f'{dif} {apibtc.get_difficulty()}\n'
#                                        f'{block} {apibtc.get_rewards()} BTC\n', reply_markup=calcmenu
#
import requests

data = requests.get(f'https://api.exchangerate.host/latest?base=USD').json()


print(round(data['rates']['RUB'],2))