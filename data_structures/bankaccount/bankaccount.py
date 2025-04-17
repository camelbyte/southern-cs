# The BankAccount class simulates a bank account.

class BankAccount:
    
    # The __init__ method accepts an argument for
    # the account's balance. It is assigned to
    # the __balance attribute.
    
    def __init__(self, bal):
        self.__balance = bal

    # The deposit method makes a deposit into the
    # account.

    def deposit(self, amount):
        self.__balance += amount

    # The withdraw method withdraws an amount
    # from the account.

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

    # The get_balance method returns the
    # account balance.

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    my_account = BankAccount(1000)

    print('Starting balance:', my_account.get_balance())

    my_account.deposit(500)
    print('After deposit:', my_account.get_balance())

    my_account.withdraw(2000)
    print('After withdrawal:', my_account.get_balance())

    print("Hey! I'm a bank account!")

    print("Hey i'm broke! ", my_account.withdraw(1000), " I have ", my_account.get_balance(), " left")
    print("Now i'm really in the hole! ", my_account.withdraw(2500), " I have ", my_account.get_balance(), " left")
