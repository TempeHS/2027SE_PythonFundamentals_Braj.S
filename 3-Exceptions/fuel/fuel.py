def main():
    try:
        numerator, denominator = input("What's the fraction? ").split("/")
        numerator = int(numerator)
        denominator = int(denominator)
    except (ValueError, ZeropercentageError):
        main()

    else:
        percentage = (numerator / denominator) * 100
        if percentage < 0 or percentage > 100:
            main()
        elif percentage == 0:
            print("E")
        elif percentage == 100:
            print("F")
        elif percentage % 1 == 0:
            print(f"{percentage:g}%")
        else:
            print(f"{round(percentage)}%")


main()
