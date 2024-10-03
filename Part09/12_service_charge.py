
class BankAccount:
    def __init__(self, owner:str, account_number:str, balance:float) -> None:
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance
        self.__service_charge()
    
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount:float):
        to_be_deposited = amount*0.99
        self.__balance += to_be_deposited

    def withdraw(self, amount:float):
        to_be_withdrawn = amount
        self.__balance -= to_be_withdrawn
    
    def __service_charge(self):
        self.__balance *= 0.99


account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)
