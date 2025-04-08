class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

personDetails = person(input("Enter your name: "), int(input("Enter your age: ")))
print(f"My name is {personDetails.name}, and I am {personDetails.age} years old.")
