# I am going to be commenting this very heavily as a tool to learn

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

deposit()
# 8:13