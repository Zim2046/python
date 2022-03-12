class Child:

    def __init__(self, name) -> None:
        self.name = name

    def play(self):
        print("I'm having fun!")


class Parent:

    children = []

    def __init__(self, name) -> None:
        self.name = name

    # instance method
    def have_child(self, child):
        Parent.children.append(child)

    @classmethod
    def print_children(cls):
        print(cls)


Parent.print_children()
mom = Parent("Mom")
Jimmy = Child('Jimmy')
Mary = Child('Mary')

mom.have_child(Jimmy)
mom.have_child(Mary)


class User:
    all_users = [all]

#     def __init__(self) -> None:
# todo Classes and Attributes

# declare a class and give it name User


class User:
    # declaring a class attribute
    population = 0

    # Thunderdome.... or something...
    def __init__(self, name, email_address):
        # Attributes
        self.name = name
        self.email = email_address
        self.account_balance = 0

    # Methods

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        # the specific user's account increases by the amount of the value
        self.account_balance += amount

    @classmethod
    def user_population(cls):
        population = population + 1

    @staticmethod
    def validate_age(age):
        is_valid = True
        if age < 18:
            is_valid = False
        return is_valid


class BankAccount:
    # class attribute
    bank_name = "First National Dojo"
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def with_draw(self, amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self

    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    # class method to get balance of all accounts

    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum

    # static methods have no access to any attribute
    # only to what is passed into it

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

        # instantiating and object from the class
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)  # output: Guido van Rossum
print(monty.name)  # output: Monty Python
print(guido.bank_name)  # output: Guido van Rossum
print(monty.bank_name)  # output: Monty Python

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)  # output: 300
print(monty.account_balance)  # output: 50
