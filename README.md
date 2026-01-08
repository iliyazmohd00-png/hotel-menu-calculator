🍽️ Miyabhai Restaurant Ordering System (Python)
Welcome to Miyabhai Restaurant Ordering System, a simple Python program that allows customers to view a menu, place multiple food orders, and receive a final bill.
This project is beginner-friendly and demonstrates basic Python concepts like dictionaries, loops, conditionals, and user input.

📌 Features


Displays a restaurant menu with prices


Accepts user input in a case-insensitive way


Allows ordering multiple items


Shows an order summary and total bill


Handles invalid menu items gracefully



🧾 Menu Items
ItemPrice (Rs)Pizza40Pasta50Chai10Nodles90Milk60Burger60Salad70Coffee80

▶️ How to Run the Program


Make sure Python 3 is installed on your system.


Copy the code into a file named, for example:
restaurant.py



Open a terminal or command prompt.


Run the program:
python restaurant.py




🧑‍🍳 How It Works (Human Explanation)


The program welcomes the user and shows the menu.


The user types the name of the item they want to order.


If the item exists:


It is added to the order


The price is added to the total




If the item does not exist:


The program shows an error message




The user types done when finished ordering.


The program displays:


All ordered items


Total amount to pay





🧪 Example Output
Welcome to Miyabhai Restaurant
--- Our Menu ---
Pizza: Rs40
Pasta: Rs50
Chai: Rs10
...
----------------

Enter the name of an item to order: pizza
✅ Pizza has been added to your order.

Enter the name of an item to order: coffee
✅ Coffee has been added to your order.

Enter the name of an item to order: done

--- Your Order Summary ---
Items ordered: Pizza, Coffee
Total amount to pay is Rs120
Thank you for visiting! ✨


🛠️ Concepts Used


Python Dictionary


while loop


if-else conditions


Lists


User input handling


String methods (lower(), capitalize())



🚀 Future Improvements (Optional Ideas)


Add quantity support


Add GST / tax calculation


Save orders to a file


Add user authentication


Create a GUI or web version





