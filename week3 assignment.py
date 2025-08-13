def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if applicable.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage to apply
    
    Returns:
    float: Final price after discount (if applicable), otherwise original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate and display the result
final_price = calculate_discount(original_price, discount_percentage)

if discount_percentage >= 20:
    print(f"Original price: ${original_price:.2f}")
    print(f"Discount applied: {discount_percentage}%")
    print(f"Final price after discount: ${final_price:.2f}")
else:
    print(f"No discount applied (needs 20% or higher). Original price: ${original_price:.2f}")