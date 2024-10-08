class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    def deposit(self, amount):
        return amount + self.account_balance
    def withdraw(self, amount):
        if self.account_balance - amount >= 0:
            return True and self.account_balance - amount
        else:
            return False
    def display_balance(self):
        print(f"Current Balance:{self.account_balance}")
