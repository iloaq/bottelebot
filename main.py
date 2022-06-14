import types
import telebot
from telebot import types
import apibtc
from database import DB
import words
import API
import apicurrency

bot = telebot.TeleBot('5505744557:AAFAF1qlsOAG3XXwhhFOTkIZbs_bUR9bDr0')
botdb = DB()
botdb.__init__()


@bot.message_handler(commands=['start'])
def start(message):
    langstart = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    ru = types.KeyboardButton('🇷🇺')
    en = types.KeyboardButton('🇺🇸')
    langstart.add(ru,en)
    msg = bot.send_message(message.chat.id, 'Выберите язык', reply_markup=langstart)
    bot.register_next_step_handler(msg, insert_data)

def insert_data(message):
    global user_id
    user_id = message.chat.id
    currency = 'RUB'
    pay = 0

    if message.text == '🇷🇺':
        language = '🇷🇺'
        botdb.insert_users(user_id,language,currency,pay)
        bot.send_message(message.chat.id, f'Выбран 🇷🇺\n Автоматически выставлены стандартные настройки:\n <b> Валюта : {botdb.select_currency(user_id)} \nЦена за кВТ/ч : {botdb.select_pay(user_id)} {botdb.select_currency(user_id)}</b>', parse_mode='html')
        menu(message)

    elif message.text == '🇺🇸':
        language = '🇺🇸'
        botdb.insert_users(user_id, language, currency, pay)
        bot.send_message(message.chat.id, f'Selected 🇺🇸\n The default settings are set automatically:\n <b> Currency : {botdb.select_currency(user_id)} \nPrice per kW/h : {botdb.select_pay(user_id)} {botdb.select_currency(user_id)}</b>', parse_mode='html')
        menu(message)

    else:
        returnstart = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,row_width=1)
        backstart = types.KeyboardButton(words.message['back'][lang])
        returnstart.add(backstart)
        msg = bot.send_message(message.chat.id, 'Ваш язык не используется', reply_markup=returnstart)
        bot.register_next_step_handler(msg, start)

@bot.message_handler(commands=['menu'])
def menu(message):
    global lang, user_id
    user_id = message.chat.id
    lang = botdb.select_lang(user_id)
    homebutton = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    calcbutton = types.KeyboardButton(words.message['calc_menu'][lang])
    settmenu = types.KeyboardButton(words.message['settings_menu'][lang])
    helpmenu = types.KeyboardButton(words.message['help_menu'][lang])
    homebutton.add(calcbutton,settmenu,helpmenu)
    msg = bot.send_message(message.chat.id, words.message['main_menu'][lang], reply_markup=homebutton)
    bot.register_next_step_handler(msg, call_menu)


def call_menu(message):
    if message.text == words.message['calc_menu'][lang] or message.text == words.message['selectotherminer'][lang]:
        minerlist = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1,one_time_keyboard=True,)
        back = types.KeyboardButton(words.message['back_menu'][lang])
        miner1 = types.KeyboardButton(words.miner['Bitmain Antminer S19j Pro 110T']['text'])
        miner2 = types.KeyboardButton(words.miner['Bitmain Antminer S19j Pro 104T']['text'])
        miner3 = types.KeyboardButton(words.miner['Bitmain Antminer S19j Pro 100T']['text'])
        miner4 = types.KeyboardButton(words.miner['Bitmain Antminer S19 86T']['text'])
        miner5 = types.KeyboardButton(words.miner['MicroBT Whatsminer M20s 68T']['text'])
        miner6 = types.KeyboardButton(words.miner['MicroBT Whatsminer M21s 54T']['text'])
        miner7 = types.KeyboardButton(words.miner['MicroBT Whatsminer M21s 56T']['text'])
        miner8 = types.KeyboardButton(words.miner['MicroBT Whatsminer M21s 58T']['text'])
        miner9 = types.KeyboardButton(words.miner['MicroBT Whatsminer M30s 86T']['text'])
        miner10 = types.KeyboardButton(words.miner['MicroBT Whatsminer M30s 88T']['text'])
        miner11 = types.KeyboardButton(words.miner['MicroBT Whatsminer M30s 100T']['text'])
        miner12 = types.KeyboardButton(words.miner['MicroBT Whatsminer M30s 102T']['text'])
        miner13 = types.KeyboardButton(words.miner['MicroBT Whatsminer M30s 106T']['text'])
        miner14 = types.KeyboardButton(words.miner['MicroBT Whatsminer M30s 108T']['text'])
        miner15 = types.KeyboardButton(words.miner['MicroBT Whatsminer M30s 110T']['text'])
        miner16 = types.KeyboardButton(words.miner['MicroBT Whatsminer M31s 72T']['text'])
        miner17 = types.KeyboardButton(words.miner['MicroBT Whatsminer M31s 78T']['text'])
        miner18 = types.KeyboardButton(words.miner['MicroBT Whatsminer M31s 80T']['text'])
        minerlist.add(back,miner1,miner2,miner3,miner4,miner5,miner6,miner7,miner8,miner9,miner10,miner11,miner12,miner13,miner14,miner15,miner16,miner17,miner18)
        msg = bot.send_message(message.chat.id, words.message['selectminer'][lang],reply_markup=minerlist)
        bot.register_next_step_handler(msg, call_minerlist)
    elif message.text == words.message['settings_menu'][lang]:
        settinglist = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
        set1=types.KeyboardButton(words.message['update_lang'][lang])
        set2=types.KeyboardButton(words.message['update_cur'][lang])
        set3=types.KeyboardButton(words.message['update_pay'][lang])
        set4=types.KeyboardButton(words.message['back_menu'][lang])
        settinglist.add(set1,set2,set3,set4)
        msg = bot.send_message(message.chat.id, words.message['settingsword'][lang], reply_markup=settinglist)
        bot.register_next_step_handler(msg, settings_list)
    elif message.text == words.message['help_menu'][lang]:
        if lang == '🇷🇺':
            bot.send_message(message.chat.id, f'Инструкция по использованию телеграм-бота\n'
                                          '\n'
                                          '\n'
                                          f'1. Бот рассчитывает доходность майнинга ВТС по умолчанию с ценой электричества 0 рублей. Чтобы ввести цену за КВт/час за электричество, перейдите в раздел Настройки и следуйте инструкции. Дробные числа указывайте через запятую.\n'
                                          '\n'
                                          f'2. Выберите из меню оборудование, которое выбираете для майнинга BTC.\n'
                                          f'\n'
                                          f'3. Бот рассчитает для Вас окупаемость инвестиций на выбранном оборудовании при текущей цене биткоина.'
                                          '\n'
                                          f'4. Закажите оборудование для майнинга, написав\n@diana_miningbtc '
                                          '\n'
                                          f'Подпишитесь на наш телеграм-канал\nhttps://t.me/mining4you_ru\nОзнакомьтесь с условиями покупки и хостинга в нашемдата-центре на нашем сайте\nhttps://mining4-you.com/'
                         )
            menu(message)
        else:
            bot.send_message(message.chat.id, f'Instructions for using the telegram bot\n'
                                              '\n'
                                              '\n'
                                              f'1. The bot calculates the profitability of BTC mining by with a default electricity price of 0 rubles. To enter the price per kWh for electricity, go to Settings and follow the instructions. Fractional Numbers specify, separated by a comma.\n'
                                              '\n'
                                              f'2. Select the equipment you want to select from the menu for BTC mining.\n'
                                              f'\n'
                                              f'The bot will calculate for you the return on investment on selected equipment at the current bitcoin price.'
                                              '\n'
                                              f'4. Order mining equipment by writing\n@diana_miningbtc '
                                              '\n'
                                              f'Subscribe to our Telegram Channel\nhttps://t.me/mining4you_ru\nCheck out the terms of purchase and hosting in ourdata center on our website\nhttps://mining4-you.com/'
                             )
            menu(message)

    elif message.text == words.message['back_menu'][lang]:
        menu(message)
    else:
        bot.send_message(message.chat.id, words.message['error'][lang])
        menu(message)


def call_minerlist(message):
    calcin = message.text

    if calcin == words.message['back_menu'][lang]:
        menu(message)

    else:
        wordsminer = words.miner[calcin]['api']
        callist = API.api_miners(wordsminer)

        if callist == '0':
            msg = bot.send_message(message.chat.id, words.message['errorminer'][lang])
            bot.register_next_step_handler(msg, call_minerlist)

        else:
            currency = botdb.select_currency(user_id)
            Minername = API.api_minerinfo(wordsminer)
            btc_th = float(0.00000461)
            pay = float(botdb.select_pay(user_id))
            data= words.message['datainfo'][lang]
            dif= words.message['difbit'][lang]
            block = words.message['block'][lang]
            btcdohod = words.message['btcdohod'][lang]
            wordcourse = words.message['courseword'][lang]
            coursetoday = words.message['courstoday'][lang]
            minermdoel = words.message['minermodel'][lang]
            paywords = words.message['paywords'][lang]
            paycena = words.message['paywcena'][lang]
            paydohod = words.message['dohod'][lang]
            payrashod = words.message['razhod'][lang]
            payprib = words.message['pribyl'][lang]
            payokup = words.message['okup'][lang]
            btcapi = float(apibtc.api_btc())
            curapi = float(apicurrency.currency_data1(currency))
            th = float(API.api_minerth(wordsminer))
            mes = float(30.33)
            dohod = int(btc_th*th*mes*btcapi*curapi)
            rashod = round(float(API.api_minerenergy(wordsminer))*24*mes*pay,2)
            cash = dohod - rashod
            minercost = apicurrency.currency_data1(currency) * API.api_minercost(wordsminer)
            okup = int(minercost / cash)
            calcmenu = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
            markup1 = types.KeyboardButton(words.message['selectotherminer'][lang])
            markup2 = types.KeyboardButton(words.message['settings_menu'][lang])
            markup3 = types.KeyboardButton(words.message['back_menu'][lang])
            calcmenu.add(markup1,markup2,markup3)
            msg = bot.send_message(message.chat.id, f'<b>{paydohod}: {dohod} {currency}</b>💰\n'
                                                    f'{payrashod}: {rashod} {currency}💵\n'
                                                    f'<b>{payprib}: {cash} {currency}</b>\n'
                                                    f'{payokup}: {okup}\n'
                                                    '\n'
                                                    f'{data}\n'
                                                    f'📆{words.time_get()}\n'
                                                    f'{minermdoel} - <b>{Minername} ({th})</b>\n'
                                                    f'{paywords} - <b>{pay} {currency}</b>📌\n'
                                                    '\n'
                                                    f'{wordcourse} 1 BTC = {round(float(apibtc.api_btc()), 2)} USD\n'
                                                    f'{coursetoday} 1$ = {apicurrency.currency_data1(currency)} {currency}\n'
                                                    f'{dif} {apibtc.get_difficulty()}\n'
                                                    f'{block} {apibtc.get_rewards()} BTC\n\n\nЗаказать майнеры @diana_miningbtc \n🌐http://mining4-you.com', reply_markup=calcmenu,parse_mode="html"
                                   )
            bot.register_next_step_handler(msg, call_menu)



def settings_list(message):
    if message.text == words.message['update_lang'][lang]:
        langset = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
        ru = types.KeyboardButton('🇷🇺')
        en = types.KeyboardButton('🇺🇸')
        langset.add(ru, en)
        msg = bot.send_message(message.chat.id, words.message['setlang'][lang], reply_markup=langset)
        bot.register_next_step_handler(msg, insert_data)
    elif message.text == words.message['update_cur'][lang]:
        curset = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
        RUB = types.KeyboardButton('RUB')
        USD = types.KeyboardButton('USD')
        EUR = types.KeyboardButton('EUR')
        KZT = types.KeyboardButton('KZT')
        curset.add(RUB,USD,EUR,KZT)
        msg = bot.send_message(message.chat.id, words.message['setcur'][lang], reply_markup=curset)
        bot.register_next_step_handler(msg, settings_cur)
    elif message.text == words.message['update_pay'][lang]:
        setpay1 = words.message['setpay'][lang]
        setpay = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
        returnpay = types.KeyboardButton(words.message['setpayback'][lang])
        setpay.add(returnpay)
        msg = bot.send_message(message.chat.id, f'{setpay1} {botdb.select_currency(user_id)} :',reply_markup=setpay)
        bot.register_next_step_handler(msg, settings_pay)

    elif message.text == words.message['back_menu'][lang]:
        menu(message)
    else:
        msg = bot.send_message(message.chat.id, words.message['errorminer'][lang])
        bot.register_next_step_handler(msg, settings_list)


def settings_lang(message):
    if message.text == '🇷🇺':
        language = '🇷🇺'
        botdb.update_lang(user_id, language)
        bot.send_message(message.chat.id,'Выбран 🇷🇺')
        menu(message)

    elif message.text == '🇺🇸':
        language = '🇺🇸'
        botdb.update_lang(user_id, language)
        bot.send_message(message.chat.id, 'selected 🇺🇸')
        menu(message)

    else:
        returnstart = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
        backstart = types.KeyboardButton(words.message['back'][lang])
        returnstart.add(backstart)
        msg = bot.send_message(message.chat.id, words.message['languagerror'][lang], reply_markup=returnstart)
        bot.register_next_step_handler(msg, settings_list)

def settings_cur(message):
    messageset = words.message['messageset'][lang]
    if message.text == 'RUB':
        currency = 'RUB'
        botdb.update_cur(user_id,currency)
        bot.send_message(message.chat.id, f'{messageset} {currency}')
        menu(message)
    elif message.text == 'USD':
        currency = 'USD'
        botdb.update_cur(user_id, currency)
        bot.send_message(message.chat.id, f'{messageset} {currency}')
        menu(message)
    elif message.text == 'EUR':
        currency = 'EUR'
        botdb.update_cur(user_id, currency)
        bot.send_message(message.chat.id, f'{messageset} {currency}')
        menu(message)
    elif message.text == 'KZT':
        currency = 'KZT'
        botdb.update_cur(user_id, currency)
        bot.send_message(message.chat.id, f'{messageset} {currency}')
        menu(message)

def settings_pay(message):
    pay = message.text
    if pay == words.message['setpayback'][lang]:
        menu(message)
    else:
        try:
            messagechange = words.message['messagchange'][lang]
            pay=float(pay)
            botdb.update_pay(user_id, pay)
            bot.send_message(message.chat.id, f'{messagechange} - {botdb.select_pay(user_id)} {botdb.select_currency(user_id)}')
            menu(message)
        except ValueError:
            errorinm = words.message['errorinm'][lang]
            msg = bot.send_message(message.chat.id, errorinm)
            bot.register_next_step_handler(msg, settings_pay)

@bot.message_handler(content_types='text')
def restart(message):
    commandre = types.ReplyKeyboardMarkup()
    but1=types.KeyboardButton('/start')
    but2=types.KeyboardButton('/menu')
    commandre.add(but2,but1)
    bot.send_message(message.chat.id,'Произошла ошибка', reply_markup=commandre)

bot.polling(none_stop=True)
