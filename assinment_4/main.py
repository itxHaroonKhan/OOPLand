"""
Class Variables and Class Methods
Assignment:
Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

"""
class Bank:
    bank_name = "First Bank of Nigeria" #class variable


    @classmethod
    def change_bank_name(cls,name):  #class method
        cls.bank_name = name





if __name__ == '__main__':
    print(f"Bank Name :{Bank.bank_name}")

    Bank.change_bank_name("Guaranty Trust Bank")

    print(f"chage bank name :{Bank.bank_name}")

