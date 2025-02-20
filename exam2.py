class Classwallet:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Add money {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Add money amount must be positive.")
            
    def spend(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Spend {amount:.2f}. Remaining balance: {self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Spend amount must be positive.")

    def display_balance(self):
        print(f"Balance for {self.owner}: {self.balance:.2f}")


account = Classwallet("09856311553", "Class Wallet", 1000)

account.display_balance()
account.add_money(100)
account.spend(150) 
account.display_balance()