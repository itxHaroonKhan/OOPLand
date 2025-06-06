"""
1 .Using self
Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

"""



class Student:
    def __init__(self,name,marks):  # ye constructor hai
        self.name = name     # ye self  instance variable hai
        self.marks = marks

    def display(self): # ye method hai
        print(f"Name: {self.name}, Marks: {self.marks}")


if __name__ == "__main__":
    student1 = Student("Haroon Rasheed" , 76)
    student1.display()














class counter:
    count = 0

    def __init__(self) :
        counter.count += 1

    @classmethod
    def sho_count(cls):
        print(f"Number of objects created: {cls.count}")


s1 = counter()
s2 = counter()

s1.sho_count()
