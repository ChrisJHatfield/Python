class User:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
        self.account = BankAccount (int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.first_name} {self.last_name}, Balance: ${self.account.balance}")
        return self

    def transfer_money(self, amount, first_name):
        self.account.withdrawal(amount)
        first_name.account.deposit(amount)

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

        # def display_account_balance(self):
        #     print(f"My account balance is: ${self.balance}")
        #     return self

        def yield_interest(self):
            if self.balance > 0:
                self.balance * self.int_rate
                return self
            else:
                print("No interest recieved due to a negative balance.")
                return self

chris = User("Chris", "Hatfield", "cjhsargeant@yahoo.com")
jackie = User("Jackie", "Hatfield", "abc_123@writerworld.com")
doug = User("Doug", "Hatfield", "dahstrk@gmaol.com")

chris.make_deposit(100).make_deposit(100).display_user_balance().make_withdrawal(50).display_user_balance
jackie.make_deposit(300).make_deposit(10).display_user_balance().make_withdrawal(350).display_user_balance
doug.make_deposit(1000).make_deposit(1000).display_user_balance().make_withdrawal(1500).display_user_balance