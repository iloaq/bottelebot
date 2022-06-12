import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('cryptobot.db', check_same_thread=False)
        self.c = self.conn.cursor()
        # self.c.execute(
        #     '''CREATE TABLE IF NOT EXISTS Miners (user_id integer, description text, costs text, total real)''')
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS Users (user_id integer, language text, currency text, pay int)''')
        self.conn.commit()

    # def insert_data(self, description, costs, total):
    #     self.c.execute('''INSERT INTO finance(description, costs, total) VALUES (?, ?, ?)''',
    #                    (description, costs, total))
    #     self.conn.commit()

    def insert_users(self, user_id, language, currency, pay):
        self.c.execute(f'''SELECT user_id FROM Users WHERE user_id = {user_id}''')
        data = self.c.fetchone()
        if data is None:
            self.c.execute('''INSERT INTO Users(user_id, language, currency, pay) VALUES (?, ?, ?, ?)''',
                           (user_id, language, currency, pay))
            self.conn.commit()

        else:
            self.c.execute('''UPDATE Users SET language= ? WHERE user_id = ? ''',
                           (language, user_id))
            self.conn.commit()

    def select_lang(self, user_id):
        self.c.execute(f'''SELECT language FROM Users WHERE user_id = {user_id}''')
        data_users: str = self.c.fetchone()
        return data_users[0]

    def select_currency(self, user_id):
        self.c.execute(f'''SELECT currency FROM Users WHERE user_id = {user_id}''')
        data_users: str = self.c.fetchone()
        return data_users[0]

    def select_pay(self, user_id):
        self.c.execute(f'''SELECT pay FROM Users WHERE user_id = {user_id}''')
        data_users: str = self.c.fetchone()
        return data_users[0]

    def update_lang(self, user_id, language):
        self.c.execute('''UPDATE Users SET language= ? WHERE user_id = ? ''',
                       (language, user_id))
        self.conn.commit()

    def update_cur(self, user_id, currency):
        self.c.execute('''UPDATE Users SET currency= ? WHERE user_id = ? ''',
                       (currency, user_id))
        self.conn.commit()

    def update_pay(self,user_id, pay):
            self.c.execute('''UPDATE Users SET pay= ? WHERE user_id = ? ''',
                           (pay, user_id))
            self.conn.commit()