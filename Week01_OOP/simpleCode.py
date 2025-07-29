class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

dog1 = Dog("Puppy")
print(dog1.bark()) 