number1 = (input("Enter the first number: "))
number2 = (input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

print(f"number1: {number1}, number2: {number2}, operation: '{operation}'")  # Debugging print

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else: 
    print("Invalid operation")


