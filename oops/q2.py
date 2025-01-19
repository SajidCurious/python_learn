# create an account with 2 attributes - balance & balance no.
# create methods for debit, credit & printing the balance.

class Account:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_no = acc_no

    def debit(self,amount):
        self.balance -= amount
        print("$.", amount, "has been debited")
        print("remaining balance is", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("$.", amount, "has been credited")
        print("remaining balance is", self.get_balance())


    def get_balance(self):
        return self.balance


s1 = Account(2050,123456789)
print(s1.balance,s1.account_no)
s1.credit(500)
s1.debit(500)
