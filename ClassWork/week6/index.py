from math import sqrt
import random

print(sqrt(16))  # This will print 4.0
print("power 2^3 is", pow (2, 3))  # This will raise an error because math is not imported

print("random number is", random.randint(1, 10))  # This will raise an error because random is not imported

print ("Random people", random.choice(["Alice", "Bob", "Charlie"]))  # This will raise an error because random is not imported