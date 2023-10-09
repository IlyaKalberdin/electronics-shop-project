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


def test_Item_name_getter(test_Item):
    test_Item.name = "Смартфон"
    assert test_Item.name == "Смартфон"

    test_Item.name = "СуперСмартфон"
    assert test_Item.name == "Смартфон"


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
    assert len(Item.all) == 5


def test_Item_instantiate_from_csv():
    """Тест для метода instantiate_from_csv класса Item"""
    Item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5


def test_Item_string_to_number():
    """Тест для метода string_to_number класса Item"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
