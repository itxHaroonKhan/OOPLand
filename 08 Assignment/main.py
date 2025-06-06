

# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.



#Parent class
class person:
    def __init__(self,name):
        self.name = name



#Child class
class Teacher(person): # inherit from person
    def __init__(self, name,subject):
        super().__init__(name)  # call the constructor of the parent class
        self.subject = subject   # super hum used to access the parent class attributes


    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")




if __name__ == "__main__":
    teachar = Teacher("Haroon","JavaScript")
    teachar.display()












