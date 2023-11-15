import decimal

class Account:
    def __init__(self, user_account_id: int, balance: decimal.Decimal):
        self._user_account_id = user_account_id
        self._balance = balance

    # Геттер для user_account_id
    def get_user_account_id(self):
        return self._user_account_id

    # Сеттер для user_account_id
    def set_user_account_id(self, user_account_id):
        self._user_account_id = user_account_id

    # Геттер для balance
    def get_balance(self):
        return self._balance

    # Сеттер для balance
    def set_balance(self, balance):
        self._balance = balance

    def add_funds(self, amount: decimal.Decimal):
        self._balance += amount