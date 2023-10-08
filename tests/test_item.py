import pytest

from src.item import Item


@pytest.fixture
def test_Item():
    test_item1 = Item("Телевизор", 49500.00, 25)

    return test_item1


def test_Item_attr(test_Item):
    """Функция для теста свойств класса Item"""
    assert test_Item.name == "Телевизор"
    assert test_Item.price == 49500.00
    assert test_Item.quantity == 25


def test_Item_calculate_total_price(test_Item):
    """Тест метода calculate_total_price класса Item"""
    assert test_Item.calculate_total_price() == 1237500.00


def test_Item_apply_discount(test_Item):
    """Тест метода apply_discount класса Item"""
    Item.pay_rate = 0.5
    test_Item.apply_discount()
    assert test_Item.price == 24750


def test_Item_all(test_Item):
    """Тест общего атрибута all класса Item"""
    assert len(Item.all) == 4
