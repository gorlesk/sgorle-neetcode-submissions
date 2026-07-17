class BankAccount:
    def __init__(self, balance: int):
        self.__bal = balance
        # Add private balance
    
    # TODO: Add getter method for balance
    def get_balance(self) -> int:
        if (self.__bal >= 0):
            return (self.__bal)
    # TODO: Add setter method for balance
    def set_balance(self, bal:int) :
        if (bal < 0):
            print ("Cannot set negative balance!")
        else:    
            self.__bal = bal



# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
