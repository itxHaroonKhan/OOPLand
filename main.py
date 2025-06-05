# University Management System

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class student(person):
    def __init__(self,  studentName, studentAge, rollNumabr,):
        super().__init__(studentName, studentAge)
        self.rollNumabr = rollNumabr
        self.courses = []


    def registerForCources(self):
        print("Available Courses:")
        print("1. Python")
        print("2. Java")
        print("3. C++")
        print("4. C")
        print("5. C#")
        print("6. JavaScript")
        print("7. PHP")
        print("8. Ruby")
        print("9. Swift")
        print("10. Go")

        a = input("Enter the course number you want to register for: ")
        if a == "1":
            self.courses.append("Python")
        elif a == "2":
            self.courses.append("Java")
        elif a == "3":
            self.courses.append("C++")
        elif a == "4":
            self.courses.append("C")
        elif a == "5":
            self.courses.append("C#")
        elif a == "6":
            self.courses.append("JavaScript")
        elif a == "7":
            self.courses.append("PHP")
        elif a == "8":
            self.courses.append("Ruby")
        elif a == "9":
            self.courses.append("Swift")
        elif a == "10":
            self.courses.append("Go")
        else:
            print("Invalid course")

        print(f" Yar Name : {self.name}\n\n Your Age: {self.age}\n\n Your RullNo : {self.rollNumabr} \n\n Registered Courses: {self.courses}")


ai = student( "Haroon Rasheed", 20  ,1)
ai.registerForCources()



