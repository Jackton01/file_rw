# Step 1: Define the function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price


# Step 2: Get input from the user
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Step 3: Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Step 4: Print the result
    if final_price < original_price:
        print(f"Discount applied! The final price is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {original_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")
