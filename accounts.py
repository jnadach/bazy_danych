class Account:

    def __init__(self, name: str, open_balance: float = 0.0):
        self.name = name
        self._balance = open_balance
        print(f"Account {name} created with opening balance {round(open_balance, 2)}")

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited to Account {self.name}")

    def withdraw(self, amount: float):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withraw from account {self.name}")
