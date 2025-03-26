age = input("Enter your age: ")
name = input("Enter your name: ")

while True:
    try:
        age = int(input("Enter your age: "))
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Please enter a valid age.")

name = input("Enter your name: ")
   
def introduce(name, age):
    return f"My name is {name}, and I'm {age} years old."

print(introduce(name, age))  # Output: My name is Bob, and I'm 25 years old.