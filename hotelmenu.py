# Define the restaurant menu with prices.
# Using lowercase keys for easier, case-insensitive matching.
menu = {
    'pizza': 40,
    'pasta': 50,
    'chai': 10,
    'nodles': 90,
     'milk': 60,
    'burger': 60,
    'salad': 70,
    'coffee': 80
}

# Greet the customer and display the menu.
print("Welcome to Miyabhai Restaurant")
print("--- Our Menu ---")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs{price}")
print("----------------")

# Initialize variables to store the total order and the list of items.
order_total = 0
items_ordered = []

# Use a while loop to allow the user to order multiple items.
while True:
    # Get user input for an item, converting to lowercase for case-insensitive matching.
    item_name = input("\nEnter the name of an item to order (or 'done' to finish): ").lower()

    # Check if the user wants to finish their order.
    if item_name == 'done':
        break  # Exit the loop

    # Check if the item is in the menu.
    if item_name in menu:
        order_total += menu[item_name]
        items_ordered.append(item_name.capitalize())
        print(f"✅ {item_name.capitalize()} has been added to your order.")
    else:
        print(f"❌ Sorry, '{item_name.capitalize()}' is not on our menu.")

# Display the final order summary and total.
print("\n--- Your Order Summary ---")
if items_ordered:
    print(f"Items ordered: {', '.join(items_ordered)}")
    # Corrected the typo in the variable name.
    print(f"Total amount to pay is Rs{order_total}")
else:
    print("You didn't order any items.")
print("Thank you for visiting! ✨")



