Assignment: User

-[]-Create a file with the User class, including the __init__ and make_deposit methods

-{}- Add a make_withdrawal method to the User class

Add a display_user_balance method to the User class

Create 3 instances of the User class

Have the first user make 3 deposits and 1 withdrawal and then display their balance

Have the second user make 2 deposits and 2 withdrawals and then display their balance

Have the third user make 1 deposits and 3 withdrawals and then display their balance

BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

For this assignment, we'll add some functionality to the User class:

make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
display_user_balance(self) - have this method print the user's name and account balance to the terminal
eg. "User: Guido van Rossum, Balance: $150
BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance