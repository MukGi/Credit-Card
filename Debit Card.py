class CreditCard:
    def __init__(self, bank, limit, account, customer):
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
    
    def charge(self, price):
        chargeAmnt = 0
        if(self._balance>price): #If customer has sufficient balance
            chargeAmnt = self._balance - price #proceed with payment
            print(chargeAmnt)
            return True
        elif(self._balance<price): #else return false
            return False
        
    def make_payment(self,amount):
        self._balance -= amount
        return self._balance