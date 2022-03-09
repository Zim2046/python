class BankAccount:

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.010, balance=0):
        # your code here! (remember, instance attributes go here);
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        # your code here
        balance += amount
        print(balance)

    def withdraw(self, amount):
        # your code here
        balance -= amount
        if balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            print(self)
        print(balance)

    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        # your code here
        pass


MyAcc = BankAccount()
