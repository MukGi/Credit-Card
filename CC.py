class CreditCard:
    def __init__(self, bank, limit, account, customer):
        self._bank = bank #Name of bank
        self._limit = limit #Credit limit
        self._accnt = account #Account name
        self._customer = customer #name of customer
        self._balance = 0