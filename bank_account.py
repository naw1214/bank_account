class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = 0
        self.balance = 0
    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def yield_interest(self, amount):
        self.int_rate = amount
        return self
    
    def display_account_info(self):
        print(f'{self.balance} at {self.int_rate}')
        return self
    

eugine = BankAccount(0,0)
thor = BankAccount(0,0)

eugine.deposit(100).deposit(100).deposit(200).withdraw(100).yield_interest(.06).display_account_info()
thor.deposit(200).deposit(300).withdraw(50).withdraw(150).withdraw(220).withdraw(450).yield_interest(.10).display_account_info()
