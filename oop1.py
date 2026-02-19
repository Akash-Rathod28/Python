class Account():
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
    #debit method
    # @staticmethod
    def debit(self,amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        # print("Total Balance = ", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs", amount, "was creadited")
    
    def get_balance(self):
        return self.balance

acc1 = Account(1000,1234)
acc1.debit(1000)
acc1.credit(1000)
