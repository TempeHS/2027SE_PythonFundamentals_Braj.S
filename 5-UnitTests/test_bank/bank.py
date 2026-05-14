def greeting(text):
    text = text.strip().lower()
    if text.startswith("hello"):
        return "$0"
    elif text.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    user_input = input("Say a greeting ")
    print(greeting(user_input))
