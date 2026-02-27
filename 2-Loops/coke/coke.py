def main():
    coke_cost = 50
    paid_amount = 0
    remaining = 50
    amount_due = 50

    while paid_amount < coke_cost:
        p_amount = int(input("Insert a coin: "))
        if p_amount != 25 and p_amount != 10 and p_amount != 5:
            print("Invalid try again! ")
        else:
            paid_amount += p_amount
            if paid_amount >= 0:
                print("Amount due:", remaining - paid_amount)
            else:
                change = coke_cost - paid_amount
                if change < 0:
                    print("Change owed:", change)


main()
