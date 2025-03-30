import datetime
import readline

# Sample customer data stored in a dictionary
# customers dictionary stores customer details Key: Customer's full name and Values: 4-digit PIN code (string) for authentication and 
customers = {
    "Avi Cohen": {"pin": "1234", "balance": 1000},
    "Yossi Cohen": {"pin": "6543", "balance": 500},
    "Yuri Levi": {"pin": "5852", "balance": 800}
}

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


# The "Other" withdrawal option now informs the user that only multiples of 20, 50, or 100 are allowed. It also gives them three attempts to enter a valid amount, displaying a warning and reducing the attempt count each time.