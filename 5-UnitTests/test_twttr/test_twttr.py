from twttr import shorten


def main():
    test()


def test():
    try:
        assert shorten("abc") == "bc"
    except AssertionError:
        print("test")


if __name__ == "__main__":
    main()
