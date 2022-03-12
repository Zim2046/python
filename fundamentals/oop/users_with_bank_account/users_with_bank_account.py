# todo BankAccount Class

import this


class BankAccount:
    # NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------
    accounts = []
    # NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------

    # don't forget to add some default values for these parameters!
    def __init__(self, accntType, int_rate, balance):
        # your code here! (remember, instance attributes go here);
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        # self.accounts[accntType] = (self)
        self.accounts.append(self)
# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------

        # We can append the current instant self to instances array
        # self.accounts.append({accntType: self.__dict__})
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
    def get_accounts(cls):
        for i in cls.accounts:
            print(i)
# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------

    @ staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

# todo User Class - - - - - - - - - - - -  - -   -   -   -   - - - - - -


class User:

    def __init__(self, name, accntType):
        # instance attributes
        self.name = name
        self.accntType = self.name + ', ' + accntType

        self.account = {self.accntType: BankAccount(
            self.accntType, int_rate=0.02, balance=0)}
        #
        print(self.account[f'{self.name}, {accntType}'].__dict__)
        # print(self.account.__dict__)

    def make_withdrawal(self, amount, accntType='Checking'):
        print(f"{self.name} made a withdrawal of ${amount}")
        BankAccount.accounts[self.accntType].balance -= amount
        return self  # put this here if you want to chain things

    def make_deposit(self, amount, accntType='Checking'):
        print(f"{self.name} made a deposit of ${amount}")
        self.account[f'{self.name}, {accntType}'].balance += amount
        # self.account[self.accntType].balance += amount
        return self  # put this here if you want to chain things

    def display_user_balance(self, accntType='Checking'):
        for i in BankAccount.accounts:
            if():

        print(
            f"{self.name}'s New Balance Is: ${ self.account[f'{self.name}, {accntType}'].balance}")
        return self  # put this here if you want to chain things
# ---  ----------------  ----------------  ----------------  ----------------  ----------------  -------------

    def transfer_money(self, person, amount, accntType=None):
        # make_withdrawal(self, amount)
        self.account[self.accntType].balance -= amount
        person.account[self.accntType].balance += amount
        print(f"{self.name} just transferred ${amount} to {person.name}")
        return self  # put this here if you want to chain things

# todo User Class - - - - - - - - - - - -  - -   -   -   -   - - - - - -


# create instances of the user
Tim = User("Tim", 'Savings')
Tim = User("Tim", "Checking")
Nibbles = User("Nibbs", "Savings")
Nibbles = User("Nibbs", "Retirement")
Savannah = User("Savannah", "Yield Farming")
Savannah = User("Savannah", "Stake Pool")

# todo User Class - - - - - - - - - - - -  - -   -   -   -   - - - - - -

Tim.display_user_balance('Savings').make_deposit(
    1000, 'Savings').display_user_balance()

# # Chaining methods togehter to accomplish withrawals, deposits, and balance displays
# Tim.display_user_balance().make_deposit(1000).make_deposit(5000).make_deposit(
#     20000).make_withdrawal(3000).display_user_balance()

# Nibbles.display_user_balance().make_deposit(10000).make_deposit(
#     5000).make_withdrawal(3000).make_withdrawal(3000).display_user_balance()

# Savannah.display_user_balance().make_deposit(40000).make_withdrawal(
#     3000).make_withdrawal(3000).make_withdrawal(3000).display_user_balance()

# Tim.transfer_money(Savannah, 10000).display_user_balance()
# Savannah.display_user_balance()

# Print to the terminal; the stored Bank Accoouts that were created from all users using the @classmethod in the BankAccount class.
print(BankAccount.get_accounts())
