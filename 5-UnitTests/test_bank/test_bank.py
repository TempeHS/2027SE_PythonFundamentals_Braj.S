from bank import greeting


def main():
    test_greeting()


def test_greeting():
    assert greeting("Hello") == "$0"


if __name__ == "__main__":
    main()
