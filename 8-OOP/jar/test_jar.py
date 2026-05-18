import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0


def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("12")


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(10)

    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(4)
    assert jar.size == 7

    with pytest.raises(ValueError):
        jar.deposit(4)


def test_withdraw():
    jar = Jar(10)

    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5

    jar.withdraw(5)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)


def test_negative_amounts():
    jar = Jar()

    with pytest.raises(ValueError):
        jar.deposit(-1)

    with pytest.raises(ValueError):
        jar.withdraw(-1)
