"""
Constructors and Destructors
Assignment:
Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


"""


class  Logger:
    def __init__(self):
        print("Hello World wilcome to python") #Constructor __init__

    def __del__(self):   #destructor  __del__
        print("Bye bye")


    def main():
        print("Hello")


if __name__ == "__main__":
    log = Logger()
    # del log

