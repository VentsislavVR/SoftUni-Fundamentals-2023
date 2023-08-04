from typing import Union


class Account:
    def __init__(self, id: int, balance: int, pin: int):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self,pin:int)->Union[str,int]:
        if self.__pin == pin:
            return self.__id
        return "Wrong pin"
    def change_pin(self,old:int,new:int):
        if old == self.__pin:
            self.__pin = new
            return "Pin changed"
        return "Wrong pin"

account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))


