number = int(input(":"))
numer2 = int(input(":"))

def large_power(base, exponent):
    return base ** exponent > 5000

# Example usage:
print(large_power(number, numer2))  # False (10^3 = 1000)
print(large_power(8, 8))  # True (20^3 = 8000)
print(large_power(4, 9))   # False (8^4 = 4096)
print(large_power(3, 5))   # True (5^5 = 3125)
