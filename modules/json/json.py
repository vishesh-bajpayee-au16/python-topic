
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def name(self):
        print(f"Your name is: {self.name}")

    def age(self):
        print(f"Your age is: {self.age}")

person1 = Person("Vishesh",22)
person1.age()
