
# 2 ) Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class counter():
    count = 0

    def __init__(self): # yee init is a constructor

        counter.count += 1

    @classmethod  # yee cls is a class method used to access class variable
    def increment_count(cls):
        print(f"Total Object Numabr {cls.count}")


obj1 = counter() # yee obj is an object
obj2 = counter()
obj3 = counter()

counter.increment_count() # yee class method is called by class name









