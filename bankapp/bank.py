
# 1- The Bank class is the main system class
# 2- Ensure that current balance is $1000, and show the current balance
# 3- Update the main( ) method in Bank to perform the following actions:
# (d) make a deposit (read amount from STDIN)
# (w) make a withdraw (read amount from STDIN)
# (s) show balance
# (x) exit the system
# NOTE:
# • Handle exceptions related to funds availability in the withdraw action
# • The Bank system should offer repeatedly the choices to customers until x is entered

class Bank:
    name = "Bank of Mars"
    def __init__(self, name=name):
        self.name = name

    def __main__(self):
        inpt = input("Enter action you would like to do (d/w/s/x): ")
        while inpt != "x":
            match inpt:
                case "d":
                    self.deposit()
                case "w":
                    self.withdraw()
                case "s":
                    self.show()
            inpt = input("Enter action you would like to do (d/w/s/x): ")

class Account:
    def __init__(self, type: str, balance: float):
        self.type = type
        self.balance = balance
        print(f"Account created, type: {self.type}. Balance: {self.balance}")

    def deposit(self):
        amt = float(input("Enter amount to deposit: "))
        self.balance += amt
        print(f"Deposited ${amt:.2f}.")

    def withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt <= self.balance:
            self.balance -= amt
            print(f"Withdrew ${amt:.2f}. Remaining balance: ${self.balance:.2f}.")
        else:
            print("Amount requested exceeds available balance.")

    def show(self):
        print(f"Available balance: ${self.balance:.2f}.")

if __name__ == "__main__":
    bank = Bank()
    bank.__main__()
    