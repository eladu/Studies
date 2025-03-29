# Save the customer data to a JSON file** on the system.
# Load the data from the JSON file when the program starts.
# When the user changes their PIN, update the JSON file with the new PIN.

import datetime
import readline
import json

# File to store customer data
CUSTOMER_DATA_FILE = "customers.json"

# Function to load customer data from the JSON file
def load_customers():
    try:
        with open(CUSTOMER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, return a default set of customers
        return {
            "Avi Cohen": {"pin": "1234", "balance": 1000},
            "Yossi Cohen": {"pin": "6543", "balance": 500},
            "Yuri Levi": {"pin": "5852", "balance": 800}
        }

# Function to save customer data to the JSON file
def save_customers(customers):
    with open(CUSTOMER_DATA_FILE, "w") as file:
        json.dump(customers, file, indent=4)

# Sample customer data stored in a dictionary
customers = load_customers()  # Load customers from the file

# Function to display a bordered message
def print_boxed_message(message):
    border = "=" * (len(message) + 4)
    print(border)
    print(f"| {message} |")
    print(border)

# Function to validate the entered PIN
def validate_pin(user, pin):
    return customers[user]["pin"] == pin  # Checks if input PIN matches stored PIN

# Function to enable user input history
def setup_input_history():
    readline.set_history_length(10)  # Store last 10 inputs

# Function to handle deposits
def deposit_money(user):
    setup_input_history()
    try:
        amount = int(input("How much would you like to deposit? "))
        if amount % 20 == 0:  # Ensures amount is a multiple of 20, 50, or 100
            customers[user]["balance"] += amount  # Adds deposit amount to balance
            save_customers(customers)  # Save changes to the file
            print_boxed_message("Deposit successful!")
        else:
            print_boxed_message("Invalid amount! Must be a multiple of 20, 50, or 100.")
    except ValueError:
        print_boxed_message("Invalid input! Please enter a valid number.")

# Function to handle withdrawals
def withdraw_money(user):
    setup_input_history()
    options = {"1": 50, "2": 100, "3": 150, "4": 300}  # Predefined withdrawal amounts
    print_boxed_message("Choose amount: 1 - 50, 2 - 100, 3 - 150, 4 - 300, 5 - Other")
    choice = input("Select an option: ")
    try:
        if choice in options:
            amount = options[choice]
        elif choice == "5":
            attempts = 3
            while attempts > 0:
                amount = int(input(f"Enter amount (must be a multiple of 20, 50, or 100): "))
                if amount % 20 == 0:
                    break
                attempts -= 1
                print_boxed_message(f"Invalid amount! You have {attempts} attempts left.")
            else:
                print_boxed_message("Too many invalid attempts. Returning to ATM menu.")
                return
        else:
            print_boxed_message("Invalid choice!")
            return
        
        if amount <= customers[user]["balance"]:  # Checks sufficient funds
            customers[user]["balance"] -= amount  # Deducts withdrawal amount from balance
            save_customers(customers)  # Save changes to the file
            print_boxed_message("Withdrawal successful!")
        else:
            print_boxed_message("Transaction failed! Insufficient balance.")
    except ValueError:
        print_boxed_message("Invalid input! Please enter a valid number.")

# Function to check account balance
def check_balance(user):
    print_boxed_message(f"Your current balance is {customers[user]['balance']} NIS")  # Displays user's balance

# Function to change PIN code
def change_pin(user):
    setup_input_history()
    new_pin = input("Enter new 4-digit PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit():  # Ensures PIN is exactly 4 digits
        customers[user]["pin"] = new_pin  # Updates PIN in customer data
        save_customers(customers)  # Save changes to the file
        print_boxed_message("PIN changed successfully!")
    else:
        print_boxed_message("Invalid PIN format!")

# Function to print a receipt with current balance and timestamp
def print_receipt(user):
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Gets current date and time
    print_boxed_message(f"Hello {user},\nAt this moment DATE: {now}\nYou have {customers[user]['balance']} NIS in your account.\nThank you for using the ATM!")

# Function to display ATM menu and handle user actions
def atm_menu(user):
    setup_input_history()
    while True:
        print_boxed_message("ATM MENU")
        print("| d - Deposit Money   |")
        print("| w - Withdraw Money  |")
        print("| c - Check Balance   |")
        print("| p - Change PIN      |")
        print("| r - Print Receipt   |")
        print("| q - Quit            |")
        print("=" * 25)
        choice = input("Select an option: ").lower()
        
        if choice == "d":
            deposit_money(user)
        elif choice == "w":
            withdraw_money(user)
        elif choice == "c":
            check_balance(user)
        elif choice == "p":
            change_pin(user)
        elif choice == "r":
            print_receipt(user)
        elif choice == "q":
            print_boxed_message(f"GOODBYE {user}, HAVE A NICE DAY")
            break
        else:
            print_boxed_message("Invalid option! Try again.")

# Main function to authenticate user and start the ATM system
def main():
    setup_input_history()
    user = input("Enter your name (First Last): ")  # Asks for full name input
    if user in customers:  # Checks if user exists in the system
        print_boxed_message(f"Welcome, {user}")
        pin = input("Enter your PIN: ")
        if validate_pin(user, pin):  # Validates PIN
            atm_menu(user)  # Proceeds to ATM menu
        else:
            print_boxed_message("Invalid PIN! Access denied.")
    else:
        print_boxed_message("User not found!")

# Program entry point
if __name__ == "__main__":
    main()

### Key Change 
# 1. **Loading and saving customer data from/to a JSON file (`customers.json`)**: 
# - The `load_customers()` function reads customer data from the JSON file
#   at the start of the program.
# - The `save_customers(customers)` function saves any changes to the 
#   `customers.json` file after updates (e.g., PIN changes).
# 2. **Customer data file**:
# - The `customers.json` file will store the user data. 
#    If the file does not exist, it will default to a set of sample customers.
# 3. **Persistent PIN changes**: 
# - When the user changes their PIN via the `change_pin()` function, the 
#   new PIN is saved to the `customers.json` file, ensuring that it 
#   persists across sessions.