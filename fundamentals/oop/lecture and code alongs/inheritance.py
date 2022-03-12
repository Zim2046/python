class CheckingAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        # code
        pass

    def withdraw(self, amount):
        # code
        pass

    def write_check(self, amount):
        # code
        pass

    def display_account_info(self):
        # code
        pass


class RetirementAccount:
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.is_roth = is_roth

    def deposit(self, amount):
        # code - assess tax if necessary
        pass

    def withdraw(self, amount):
        # code - assess penalty if necessary
        pass

    def display_account_info(self):
        # code
        pass

# Parent class


class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance


'''
                👇🏼
'''


class BankAccount:
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self


'''
                👇🏼 Ddd logic
'''


class BankAccount:
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self


class CheckingAccount(BankAccount):
    pass


class RetirementAccount(BankAccount):
    pass


'''
                👇🏼
'''


class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth


'''
                👇🏼 Add logic
'''


class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self


'''
                👇🏼
'''


class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self


'''
👇🏼
'''
