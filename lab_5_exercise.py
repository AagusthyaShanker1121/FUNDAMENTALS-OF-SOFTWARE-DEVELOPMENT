import time
import sys

class Customer():
    def __init(self):
        pass

    def menu(self):
        user_reference()    
        while(True):
            command = user_input('command')
            match command:
                case 'd': 
                    deposit_amt = user_input("funds_deposit")
                    Bank.deposit(deposit_amt=deposit_amt)
                    print(f"${deposit_amt} deposited successfully !")
                    
                
                case 'w':
                    withdraw_amt = user_input("funds_withdraw")
                    Bank.withdraw(withdraw_amt=withdraw_amt)
                
                case 's':
                    Bank.show()
                
                case 'x':
                    type("Exiting the current session........")
                    print(f"Thank you for banking with us !!")
                    return
     
                case default:
                    pass


class Bank():
    def __init__(self, **kwargs):
        self.balance = kwargs['account_balance']
        self.customers: Customer = [Customer(name = "John Smith")] 

    def deposit(self, deposit_amt):
        # Adds the deposit amount to total balance and prints the message of amount deposited and new total balance
        self.balance += deposit_amt  
    def withdraw(self, withdraw_amt):
        # deducts withdrawal amount from acocunt balance and prints the message
        if self.balance >= withdraw_amt:
            self.balance -= withdraw_amt
            print(f"${withdraw_amt} withdrawed successfully !")
        else:
            print("withdrawn amount is more than the balance")
    def show(self):
        # Displays the current acccount balance of user along with user details
        print(f'Account balance: ${self.balance}')
    
    

    


class Account():
    def __init__(self, **kwargs):
        '''
        parameters: type:str and balance: float
        '''
        

def user_input(input_str):
    match(input_str):
        case 'funds_account':
            funds = float(input("Enter your intital account balance:\t"))
            return funds
        
        case 'funds_deposit':
            funds = float(input("Enter funds to deposit in account:\t"))
            return funds
        
        case 'funds_withdraw':
            funds = float(input("Enter funds to withdraw from account:\t"))
            return funds
        case 'command': 
            command = input('Enter command (d/w/s/x):\t')
            while command not in ['d', 'w', 's', 'x']:
                retype_command = input("Please enter valid inputs (d/w/s/x) or type 'h' for help:\t").lower()
                if retype_command == 'h':
                    user_reference()
                command = retype_command
            return command


def user_reference():

    #Prints all acceptable user commands
    print("-" * 20)
    print("User reference list:")
    print("Type 'd' to make a deposit")
    print("Type 'w' to make a withdraw")
    print("Type 's' to show balance")
    print("Type 'x' to exit the system")
    print("Type h for help")
    print("-" * 20)


def type(str):
    for letter in str:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.05)






Bank(account_balance = user_input("funds_account"))
