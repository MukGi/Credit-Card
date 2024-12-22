class CreditCard:
    def __init__(self, bank, limit, account, customer):
        """
        Leading underscores means that the variables are private
        """
        self._bank = bank #Name of bank
        self._limit = limit #Credit limit
        self._accnt = account #Account name
        self._customer = customer #name of customer
        self._balance = 0

    def get_customer(self):
        """
        Returns the customer name
        """
        return self._customer
    
    def get_balance(self):
        #gets customer balance
        return self._balance
    
    def get_account(self):
        #gets customer account
        return self._accnt
    
    def get_bank(self):
        #gets customer bank
        return self._bank
    
    def get_limit(self):
        #gets customer limit
        return self._limit
    
    def charge(self, price):
        """
        If payment charge exceeds the credit limit, then you should return false else true
        """
        if self._balance+price>self._limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self,amount):
        self._balance -= amount
        return self._balance
        