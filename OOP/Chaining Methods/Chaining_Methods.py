class User:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.first_name} {self.last_name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, amount, first_name):
        self.account_balance -= amount
        first_name.account_balance += amount

chris = User("Chris", "Hatfield", "cjhsargeant@yahoo.com")
chris.display_user_balance()
jackie = User("Jackie", "Hatfield", "abc_123@writerworld.com")
print(jackie.first_name, jackie.last_name)
doug = User("Doug", "Hatfield", "dahstrk@gmaol.com")
print(doug.first_name, doug.last_name)

chris.make_deposit(100).make_deposit(120).make_deposit(140).make_withdrawal(202).display_user_balance()
jackie.make_deposit(50).make_deposit(4000).make_withdrawal(8).make_withdrawal(1500).display_user_balance()
doug.make_deposit(3000).make_withdrawal(1000).make_withdrawal(500).make_withdrawal(700).display_user_balance()
jackie.transfer_money(250, chris)
jackie.display_user_balance()
chris.display_user_balance()