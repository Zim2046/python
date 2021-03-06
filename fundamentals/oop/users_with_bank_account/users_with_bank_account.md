Assignment: Users with Bank Accounts

Objectives:

- Practice writing classes with associations

- Update your existing User class to have an association with the BankAccount class. You should not have to change anything in the BankAccount class. The method signatures of the User class (the first line of the method with the def keyword) should also remain the same.

- But our User class no longer has a self.account_balance attribute. Instead, we have replaced this with an instance of a BankAccount by the name of self.account. That means our make_deposit (and other methods referencing self.account_balance) need to be updated! That's the goal of this assignment.

- Remember in our User methods, we can now access the BankAccount class through our self.account attribute.

- [x] **Update the User class __init__ method**

- [x] Update the User class make_deposit method

- [x] Update the User class make_withdrawal method

- [x] Update the User class display_user_balance method

- [] SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to