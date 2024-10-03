class computer:
    def __init__(self):
        self.__max_price = 100

    def sell(self):
        print(f"S.p of this computer is {self.__max_price}")

    def  price(self,price):
        self.__max_price = price

obj1 = computer()
obj1.sell()

obj1.__max_price = 150
obj1.sell()

obj1.price(200)
obj1.sell()

