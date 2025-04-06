file = open("trial.txt", "w")
data = file.write("This is a test file.")

file = open("trial.txt", "r")
data = file.read()
print(data)