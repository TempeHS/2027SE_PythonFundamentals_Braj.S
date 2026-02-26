def main():
    userInput = input("What is your name? ")
    snake(userInput)


def snake(case):
    for i in case:
        if i.isupper():
            print("_" + i.lower(), end="")
        else:
            print(i, end="")
    print()


main()
