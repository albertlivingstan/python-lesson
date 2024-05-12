class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("name:", self.name)
        print("age:", self.age)

person1 = Person("albert", 30)        
person1.info()
