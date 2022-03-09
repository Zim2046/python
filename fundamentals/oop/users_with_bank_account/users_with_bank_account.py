# todo BankAccount Class

class BankAccount:
    # NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------
    accounts = {}
# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance, accnt_key, accnt_name):
        # your code here! (remember, instance attributes go here);
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts[accnt_key] = str(self.__dict__)
# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------
        # We can append the current instant self to instances array
        # self.accounts.append(self.__dict__)
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
    # def get_accounts(cls, account_name_key):
    #     return BankAccount.accounts.get(account_name_key)
    def iterateDictionary(cls, accounts):
        for index in range(len(accounts)):
            array = []
            for k, v in accounts[index].items():
                a = "{}".format(k)
                b = "{}".format(v)
                c = '{}, {}'.format(a, b)
                array.append(c)
            # print(f"{array[0]}, {array[1]}")
            print(f'{array[0]}, {array[1]}')
            # for i in cls.instances:
            #     print(i)
            #     pass
# NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS ----------- NINJA BONUS -----------

    @ staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

# todo User Class


class User:

    accounts = []

    def __init__(self, name, typeAccount) -> None:
        # instance attributes
        self.name = name
        self.typeAccount = typeAccount
        self.account = BankAccount(
            int_rate=0.02, balance=0,  accnt_key=self.typeAccount, accnt_name=self.name)

        # instance methods
    # def make_new_account(self, newName):
    #     self.account = BankAccount(
    #         int_rate=0.02, balance=0, newName)
        # self.account.accnt_name()

    def make_withdrawal(self, amount):
        print(f"{self.name} made a withdrawal of ${amount}")
        self.account.balance -= amount
        return self  # put this here if you want to chain things

    def make_deposit(self, amount):
        print(f"{self.name} made a deposit of ${amount}")
        self.account.balance += amount
        return self  # put this here if you want to chain things

    def display_user_balance(self):
        print(f"{self.name}'s New Balance Is: ${self.account.balance}")
        return self  # put this here if you want to chain things
# BONUS-------------BONUS-------------BONUS-------------BONUS-------------BONUS-------------BONUS-------------

    def transfer_money(self, person, amount):
        # make_withdrawal(self, amount)
        self.account.balance -= amount
        person.account.balance += amount
        print(f"{self.name} just transferred ${amount} to {person.name}")
        return self  # put this here if you want to chain things


# create instances of the user
Tim = User("Tim", "Savings")
Tim = User("Tim", "Checking")
Nibbles = User("Nibbs", "Savings")
Savannah = User("Savannah", "Savings")

Tim.display_user_balance().make_deposit(1000).make_deposit(5000).make_deposit(
    20000).make_withdrawal(3000).display_user_balance()

Nibbles.display_user_balance().make_deposit(10000).make_deposit(
    5000).make_withdrawal(3000).make_withdrawal(3000).display_user_balance()

Savannah.display_user_balance().make_deposit(40000).make_withdrawal(
    3000).make_withdrawal(3000).make_withdrawal(3000).display_user_balance()

Tim.transfer_money(Savannah, 10000).display_user_balance()
Savannah.display_user_balance()

# print(BankAccount.get_accounts("Tim"))
# print(BankAccount.accounts.iterateDictionary())
print(Tim.iterateDictionary())
