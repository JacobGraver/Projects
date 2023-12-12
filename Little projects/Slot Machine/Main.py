def deposit():
    while True:
        amount = input("What is the amount that you would like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a positive number.")
        else:
            print("Please enter a number.")
    return amount

deposit()
# 8:13