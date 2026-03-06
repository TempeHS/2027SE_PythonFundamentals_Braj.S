def main():
    try:
        numerator, denominator = input("What's the fraction? ").split("/")
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError:
        main()

    else:
        if denominator == 0:
            main()
        else:
            division = numerator / denominator
            percentage = (division) * 100
            if division < 0 or division > 1:
                main()
            elif division == 0:
                print("E")
            elif division == 1:
                print("F")
            elif percentage % 1 == 0:
                print(f"{percentage:g}%")
            else:
                print(f"{round(percentage)}%")


main()
