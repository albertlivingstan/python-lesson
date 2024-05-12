class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # Animals don't necessarily make a sound

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating instances of the subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling methods
print(dog.name, "says:", dog.make_sound())
print(cat.name, "says:", cat.make_sound())
