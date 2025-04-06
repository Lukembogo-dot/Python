def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)  # Apply discount
    return price  # Return original price if discount is less than 20%

# Get user input
price = float(input("Enter the item price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print result
print(f"Price after discount is: {final_price:.2f}")
