class BankAccount:

    def __init__(self, accountNumber, balance, roi):
        self.accountNumber = accountNumber
        self.balance = balance
        self.roi = roi

    def getSimpleInterest(self, years):
        return (self.balance*self.roi*years)//100
    
    def getBalanceWithInterest(self, years):
        return self.balance + self.getSimpleInterest(years)
    

ba=BankAccount(1234,1000,4)
print(ba.getSimpleInterest(4))
print(ba.getBalanceWithInterest(4))