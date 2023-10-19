from src.phone import Phone
import pytest


@pytest.fixture
def phone_test():
    return Phone("IPhone", 100000, 40, 2)


def test_repr(phone_test):
    """
    Функция для теста метода __add__ класса Phone
    """
    assert repr(phone_test) == "Phone('IPhone', 100000, 40, 2)"


def test_number_of_sim(phone_test):
    """
    Функция для теста метода приватного аргумента number_of_sim класса Phone
    """
    phone_test.number_of_sim = 3
    assert phone_test.number_of_sim == 3

    phone_test.number_of_sim = 4.5
    assert phone_test.number_of_sim == 3
