# I am going to be commenting this very heavily as a tool to learn

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

# collect deposit // create function
def deposit():
    # while loop
    while True:
        amount = input("What is the amount that you would like to deposit? $")
        # checking that what they input is a number
        if amount.isdigit():
            # changing from a string to a number
            amount = int(amount)
            if amount > 0:
                # if the amount is greater than 0 it will leave the loop
                break
            else:
                # if it is not greater than 0
                print("Enter a positive number.")
        else:
            # if it is not a number
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        # checking that what they input is a number
        if lines.isdigit():
            # changing from a string to a number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                # if the amount is greater than or equal to 1 and less than or equal to MAX_LINES it will leave the loop
                break
            else:
                # if it is not greater than 0
                print("Enter a valid number of lines.")
        else:
            # if it is not a number
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        # checking that what they input is a number
        if amount.isdigit():
            # changing from a string to a number
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                # if the amount is greater than 0 it will leave the loop
                break
            else:
                # if it is not greater than 0
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            # if it is not a number
            print("Please enter a number.")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()