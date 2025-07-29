class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Cat(Animal):
    def says(self):
        return f"{self.name} says meow"
    
    # def speak(self):
    #     return f"{self.name} says meow"

cat1 = Cat("Whiskers")
print(cat1.speak())  # Whiskers says meow
print(cat1.says())
