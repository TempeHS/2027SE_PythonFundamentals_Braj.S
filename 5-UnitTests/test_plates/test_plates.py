from plates import is_valid


def test_valid_plates():
    assert is_valid("CS") is True
    assert is_valid("CS50") is True
    assert is_valid("HELLO") is True
    assert is_valid("WORLD6") is True


def test_too_short_or_long():
    assert is_valid("C") is not True
    assert is_valid("ABCDEFG") is not True


def test_first_two_letters():
    assert is_valid("1CS50") is not True
    assert is_valid("C550") is not True


def test_numbers_at_end():
    assert is_valid("CS50A") is not True
    assert is_valid("CS5A0") is not True


def test_no_leading_zero():
    assert is_valid("CS05") is not True
    assert is_valid("CS0") is not True


def test_only_alphanumeric():
    assert is_valid("CS 50") is not True
    assert is_valid("CS-50") is not True
    assert is_valid("CS!50") is not True
