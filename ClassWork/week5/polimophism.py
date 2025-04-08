class Dog:
    def speak(self):
        return "Woof! Woof!"
    
class Cat:
    def speak(self):
        return "Meow! Meow!"

for animal in [Dog(), Cat()]:
    dog = Dog()
    cat = Cat()
    print(dog.speak())