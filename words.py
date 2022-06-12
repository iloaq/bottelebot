import time

message = {'calc_menu': {'🇷🇺': 'Расчет доходности', '🇺🇸': 'Calculation of profitability'}, 'settings_menu':{'🇷🇺': 'Настройки', '🇺🇸':'settings'}, 'help_menu': {'🇷🇺': 'Помощь', '🇺🇸': 'Help'}, 'main_menu':{'🇷🇺': 'Главное меню', '🇺🇸': 'Main menu'},'datainfo':{'🇷🇺': 'Расчет на дату и время:', '🇺🇸': 'Calculation by date and time:'}, 'difbit':{'🇷🇺': 'Сложность сети Bitcoin:', '🇺🇸': 'Bitcoin network complexity:'},'block':{'🇷🇺': 'Награда за блок:', '🇺🇸': 'Block Reward:'},
           'btcdohod': {'🇷🇺': 'Доходность (BTC) с 1 TH/s:', '🇺🇸': 'Payout (BTC) from 1 TH/s:'},'courseword': {'🇷🇺': 'Расчёт по курсу Binance', '🇺🇸': 'Calculation at the rate of Binance'}, 'courstoday': {'🇷🇺': 'Курс ', '🇺🇸': 'Currency '},'minermodel': {'🇷🇺': 'Модель майнера', '🇺🇸': 'Miner model'},'paywords': {'🇷🇺': 'При указанной цене за кВТ/ч', '🇺🇸': 'At the given price per kW/h'},'paywcena': {'🇷🇺': 'Цена в', '🇺🇸': 'Price in'},'dohod': {'🇷🇺': 'Доход в месяц', '🇺🇸': 'Income per month'},'razhod': {'🇷🇺': 'Расход за месяц', '🇺🇸': 'Consumption per month'},'pribyl': {'🇷🇺': 'Прибыль в месяц', '🇺🇸': 'Profit per month'},'okup': {'🇷🇺': 'Окупаемость, месяцев', '🇺🇸': 'Payback, months'},
           'update_lang': {'🇷🇺': 'Изменить язык', '🇺🇸': 'Change language'}, 'update_cur': {'🇷🇺': 'Изменить валюту', '🇺🇸': 'Change currency'}, 'update_pay': {'🇷🇺': 'Изменить цену за электроэнергию', '🇺🇸': 'Change the price of electricity'}, 'back_menu': {'🇷🇺': 'Назад в меню', '🇺🇸': 'Back to menu'},
           'languagemes': {'🇷🇺': 'Выберите язык', '🇺🇸': 'Select language'},'languagerror': {'🇷🇺': 'Ваш язык не используется', '🇺🇸': 'Your language is not used'}, 'back': {'🇷🇺': 'Назад', '🇺🇸': 'Back'}, 'selectminer': {'🇷🇺': 'Выберите модель майнера', '🇺🇸': 'Select Miner Model'},
           'settingsword': {'🇷🇺': 'Настройки', '🇺🇸': 'Settings'},'error': {'🇷🇺': 'Неизвестная команда', '🇺🇸': 'Unknown command'},'errorminer': {'🇷🇺': 'Данная модель отсутствует', '🇺🇸': 'This model is not available'},'setlang': {'🇷🇺': 'Выберите язык', '🇺🇸': 'Select a language'},'setcur': {'🇷🇺': 'Выберите валюту', '🇺🇸': 'Select currency'},'setpay': {'🇷🇺': 'Введите сумму оплаты в', '🇺🇸': 'Enter payment amount in'},'setpayback': {'🇷🇺': 'Отменить ввод', '🇺🇸': 'Cancel input'},'messageset': {'🇷🇺': 'Выбран', '🇺🇸': 'Selected'},'messagchange': {'🇷🇺': 'Оплата изменена в', '🇺🇸': 'Payment has been changed to'},'errorinm': {'🇷🇺': 'Ошибка ввода', '🇺🇸': 'Input error'},
           'selectotherminer': {'🇷🇺': 'Выбрать другой майнер', '🇺🇸': 'Select another miner'},}

miner = {'Bitmain Antminer S19j Pro 110T':{'text':'Bitmain Antminer S19j Pro 110T','api':'antminer-s19j-pro-110th'},
         'Bitmain Antminer S19j Pro 104T': {'text': 'Bitmain Antminer S19j Pro 104T', 'api': 'antminer-s19j-pro-104th'},
         'Bitmain Antminer S19j Pro 100T': {'text': 'Bitmain Antminer S19j Pro 100T', 'api': 'antminer-s19j-pro-100th'},
         'Bitmain Antminer S19 86T': {'text': 'Bitmain Antminer S19 86T', 'api': 'antminer-s19'},
         'MicroBT Whatsminer M20s 68T': {'text': 'MicroBT Whatsminer M20s 68T', 'api': 'whatsminer-m20s'},
         'MicroBT Whatsminer M21s 54T': {'text': 'MicroBT Whatsminer M21s 54T', 'api': 'whatsminer-m21s'},
         'MicroBT Whatsminer M21s 56T': {'text': 'MicroBT Whatsminer M21s 56T', 'api': 'whatsminer-m21s-2'},
         'MicroBT Whatsminer M21s 58T': {'text': 'MicroBT Whatsminer M21s 58T', 'api': 'whatsminer-m21s-3'},
         'MicroBT Whatsminer M30s 86T': {'text': 'MicroBT Whatsminer M30s 86T', 'api': 'whatsminer-m30s'},
         'MicroBT Whatsminer M30s 88T': {'text': 'MicroBT Whatsminer M30s 88T', 'api': 'whatsminer-m30s-2'},
         'MicroBT Whatsminer M30s 100T': {'text': 'MicroBT Whatsminer M30s 100T', 'api': 'whatsminer-m30s-3'},
         'MicroBT Whatsminer M30s 102T': {'text': 'MicroBT Whatsminer M30s 102T', 'api': 'whatsminer-m30s-4'},
         'MicroBT Whatsminer M30s 106T': {'text': 'MicroBT Whatsminer M30s 106T', 'api': 'whatsminer-m30s-5'},
         'MicroBT Whatsminer M30s 108T': {'text': 'MicroBT Whatsminer M30s 108T', 'api': 'whatsminer-m30s-6'},
         'MicroBT Whatsminer M30s 110T': {'text': 'MicroBT Whatsminer M30s 110T', 'api': 'whatsminer-m30s-7'},
         'MicroBT Whatsminer M31s 72T': {'text': 'MicroBT Whatsminer M31s 72T', 'api': 'whatsminer-m31s'},
         'MicroBT Whatsminer M31s 78T': {'text': 'MicroBT Whatsminer M31s 78T', 'api': 'whatsminer-m31s-2'},
         'MicroBT Whatsminer M31s 80T': {'text': 'MicroBT Whatsminer M31s 80T', 'api': 'whatsminer-m31s-3'},

         }

def time_get():
    sec = time.time()
    date=time.localtime(sec)
    date = time.strftime('%d.%m.%Y %H:%M:%S', date)
    return date