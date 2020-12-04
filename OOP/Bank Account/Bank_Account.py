class BankAccount:
        def __init__(self, int_rate, balance):
            self.int_rate = int_rate
            self.balance = balance
        def deposit(self, amount):
            self.balance += amount
            return self

        def withdrawal(self, amount):
            self.balance -= amount
            if self.balance <= 0:
                print("Insufficient funds: Charging a $5 fee.")
                self.balance - 5
            return self

        def display_account_balance(self):
            print(f"My account balance is: ${self.balance}")
            return self

        def yield_interest(self):
            if self.balance > 0:
                self.balance * self.int_rate
                return self
            else:
                print("No interest recieved due to a negative balance.")
                return self

first_bank_account = BankAccount(0.03, 250)
print(first_bank_account.int_rate, first_bank_account.balance)
second_bank_account = BankAccount(0.01, 25)
print(second_bank_account.int_rate, second_bank_account.balance)
first_bank_account.deposit(150).deposit(100).deposit(50).withdrawal(70).yield_interest().display_account_balance()
second_bank_account.deposit(20).deposit(15).withdrawal(5).withdrawal(10).withdrawal(50).yield_interest().display_account_balance()