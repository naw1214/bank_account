class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else: 
            print('You have insuffcient funds')
            self.balance -= 5
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self
    
    @classmethod
    def print_info(cls):
        for account in cls.accounts:
            account.display_account_info()

savings = BankAccount(0.5,3000)
checking = BankAccount(0.2,900)

savings.deposit(100).deposit(100).deposit(200).withdraw(100).yield_interest().display_account_info()
checking.deposit(200).deposit(300).withdraw(50).withdraw(150).withdraw(220).withdraw(450).yield_interest().display_account_info()

BankAccount.print_info()