class Person:
    def __init__(self,firstname,lastname,age,number):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age 
        self.number = number 

    def fullName(self):
        print(f"FullName is: {self.firstname} {self.lastname}")
    
    def retirementAge(self):
        print(f"Retirement age: {65 - self.age}")
    

person1 = Person("Vishesh","Bajpayee",22,7987852367)

class Student(Person):
    def __init__(self,firstname,lastname,age,number,marks):
        super().__init__(firstname,lastname,age,number)
        self.marks = marks

    def marks(self):
        return self.marks

student1 = Student("vishu","bajpayee",22,123,99)
