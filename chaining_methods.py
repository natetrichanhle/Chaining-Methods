class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def make_withdrawal(self,amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print('User: ', self.name, ', Balance: ', self.balance)
        return self
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.balance += amount
        return self
p1 = User('Nate', 5000)
p2 = User('Steph', 2000)
p1.make_withdrawal(200).transfer_money(p2,200).display_user_balance()
p2.display_user_balance()