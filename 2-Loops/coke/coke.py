def main():
    coke_cost = 50
    paid_amount = 0
    remaining = 50
    amount_due = 50

    while paid_amount < coke_cost:
        p_amount = int(input("Insert a coin: "))
        if p_amount != 25 and p_amount != 10 and p_amount != 5:
            print("Amount Due:", 50 - paid_amount)
        else:
            paid_amount += p_amount
            remaining = coke_cost - paid_amount
            if remaining > 0:
                print("Amount due:", 50 - paid_amount)
    else:
        print("Change Owed:", (amount_due - paid_amount) * -1)


main()
