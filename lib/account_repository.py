from lib.account import *

class AccountRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM accounts')
        accounts = []

        for row in rows:
            accounts.append(Account(row['id'], row['email'], row['username']))

        return accounts

    def find(self, id):
        row = self._connection.execute(f'SELECT * FROM accounts WHERE id = {id}')[0]

        return Account(row['id'], row['email'], row['username'])