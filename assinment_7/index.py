# ------------------------------   Encapsulation ------------------------------ #



# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.






class Employee:
    def __init__(self, name,salary , ssn ):
        self.name = name      # public
        self._salary = salary #protected
        self.__ssn = ssn  #private




if __name__ == '__main__':
    emp = Employee("Haroon Rasheed", 10000, 123456789)
    print(f"Name: {emp.name}") #public variable
    print(f"Salary: {emp._salary}") #protected variable


    try:
        print(f"SSN: {emp.__ssn}") #private variable
    except AttributeError:
        print("Private variable can't be accessed")













