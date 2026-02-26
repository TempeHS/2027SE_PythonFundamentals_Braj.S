def main():
    amountInput = float(input("How much money would you like to deposit?"))
    total(amountInput)


def total(amount):

    while amount != 0.25 and amount != 0.10 and amount != 0.05:
        main()
    else:
        remaining = 0.50 - amount
        if remaining < 0.50:
            print(remaining)


main()
