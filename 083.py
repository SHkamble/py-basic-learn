class BAnkAccount:
    def __init__(self):
        self .balance =0  # Instance Variable (You can access it via only Object)


    def deposit (self ,amount):  # Public Function
        # self.balance = self .balance + amount
        self .balance =+ amount

    def _withdraw(self ,amount):
        self.balance -= amount

    def _show_balance(self):
     print("Your bal",self.balance)

    def Is_Auth_true_show_bal(self, isAuth):
        if isAuth:
            self._show_balance()
        else:
            print("You are not Auth")


jp_chase = BAnkAccount()
jp_chase.deposit(100000000000)
jp_chase._withdraw(4190000)   # Not a Good practice (Protected)
# jp_chase_show_balance()

# Write the code to Auth
jp_chase.Is_Auth_true_show_bal(True)
