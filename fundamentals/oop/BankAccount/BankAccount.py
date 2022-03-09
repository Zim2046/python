
class BankAccount:
    # NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------
    instances = []
# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.010, balance=0):
        # your code here! (remember, instance attributes go here);
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------
        # We can append the current instant self to instances array
        self.instances.append(self.__dict__)
# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self  # put this here if you want to chain things

    def withdraw(self, amount):
        # your code here
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
        return self  # put this here if you want to chain things

    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")
        return self  # put this here if you want to chain things

    def yield_interest(self):
        # your code here
        if self.balance >= 0:
            self.balance += (self.balance * self.int_rate)
            # print(f"Your yielded interest is {self.balance * self.int_rate}")
        return self  # put this here if you want to chain things

# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------
    @classmethod
    def get_inst(cls):
        for i in cls.instances:
            print(i)
# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------

    @ staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


Tim_Accnt = BankAccount(0.1, 50000)
Savy_Accnt = BankAccount(0.01, 100000)

Tim_Accnt.deposit(3000).deposit(10000).deposit(10000).withdraw(
    5000).yield_interest().display_account_info()

Savy_Accnt.deposit(3000).deposit(10000).withdraw(5000).withdraw(
    5000).withdraw(5000).withdraw(5000).yield_interest().display_account_info()

# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------
print(BankAccount.get_inst())
# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------
