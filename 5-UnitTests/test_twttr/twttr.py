def main():
    text = input("What's your tweet? ")
    for i in text:
        print(f"{shorten(text)}", end="")
    print()


def shorten(text):
    new_text = str()
    for i in text:
        if (
            i.lower() == "a"
            or i.lower() == "e"
            or i.lower() == "i"
            or i.lower() == "o"
            or i.lower() == "u"
        ):
            continue
        else:
            new_text += i

    return new_text


if __name__ == "__main__":
    main()
