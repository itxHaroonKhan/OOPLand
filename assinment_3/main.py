"""
3 )  Public Variables and Methods
Assignment:
Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

 """

class car():
    def __init__(self,brand) :  # public variable
        self.brand = brand

    def shart(self):
        print(f"the brand of car is {self.brand}")  # public method

if __name__ == "__main__":
    car1 = car("honda")
    car1.shart()
