class User:

    def __init__(self, account_balance, name) -> None:
        self.account_balance = account_balance
        self.name = name

    def make_withdrawal(self, amount):
        print(f"{self.name} made a withdrawal of ${amount}")
        self.account_balance -= amount
        return self  # put this here if you want to chain things

    def make_deposit(self, amount):
        print(f"{self.name} made a deposit of ${amount}")
        self.account_balance += amount
        return self  # put this here if you want to chain things

    def display_user_balance(self):
        print(f"{self.name}'s New Balance Is: ${self.account_balance}")
        return self  # put this here if you want to chain things
# BONUS-------------BONUS-------------BONUS-------------BONUS-------------BONUS-------------BONUS-------------

    def transfer_money(self, person, amount):
        # make_withdrawal(self, amount)
        self.account_balance -= amount
        person.account_balance += amount
        print(f"{self.name} just transferred ${amount} to {person.name}")
        return self  # put this here if you want to chain things


Tim = User(0, "Tim")
Nibbles = User(0, "Nibbs")
Savannah = User(0, "Savannah")

Tim.display_user_balance().make_deposit(1000).make_deposit(5000).make_deposit(
    20000).make_withdrawal(3000).display_user_balance()

Nibbles.display_user_balance().make_deposit(10000).make_deposit(
    5000).make_withdrawal(3000).make_withdrawal(3000).display_user_balance()

Savannah.display_user_balance().make_deposit(40000).make_withdrawal(
    3000).make_withdrawal(3000).make_withdrawal(3000).display_user_balance()

Tim.transfer_money(Savannah, 10000).display_user_balance()
Savannah.display_user_balance()
