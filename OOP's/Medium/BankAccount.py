class BankAccount:
    def __init__(self, accNo, balance):
        self.accNo = accNo
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance
    def get_accNo(self):
        return self.accNo
    
abhi=BankAccount(123456789, 1000)
print(abhi.get_accNo())
abhi.deposit(500)
print(abhi.get_balance())
abhi.withdraw(1000)
print(abhi.get_balance())
