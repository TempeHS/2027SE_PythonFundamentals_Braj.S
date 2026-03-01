def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if characters(s) == True and length(s) == True:
        return True


def length(c):
    letter_count = 0
    for letters in c:
        if letters.isalnum():
            letter_count += 1
    return letter_count <= 6


def characters(c):
    letter_count = 0
    for letters in c:
        if letters.isalpha():
            print(letters)
            letter_count += 1
    return letter_count >= 2


main()
