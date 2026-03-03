def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        first_characters(s) == True
        and length(s) == True
        and number_order(s) == True
        and numbers_at_end(s) == True
    ):
        return True


def length(c):
    letter_count = 0
    for letters in c:
        if letters.isalnum():
            letter_count += 1
    return letter_count <= 6 and c.isalnum()


def first_characters(c):
    if len(c) >= 2 and c[:2].isalpha():
        return True


def number_order(c):
    for ch in c:
        if ch.isdigit():
            return ch != "0"
    return True


def numbers_at_end(c):
    seen_digit = False

    for ch in c:
        if ch.isdigit():
            seen_digit = True
        elif seen_digit and ch.isalpha():
            return False

    return True


main()
