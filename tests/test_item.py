from src.item import Item


def test_Item():
    """Функция для теста класса Item"""
    test_item1 = Item("Телевизор", 49500.00, 25)

    # Тест атрибутов
    assert test_item1.name == "Телевизор"
    assert test_item1.price == 49500.00
    assert test_item1.quantity == 25

    # Тест метода calculate_total_price
    assert test_item1.calculate_total_price() == 1237500.00

    # Тест метода apply_discount
    Item.pay_rate = 0.5
    test_item1.apply_discount()
    assert test_item1.price == 24750

    # Тест общего атрибута класса
    test_item2 = Item("Наушники", 15000, 5)

    assert len(Item.all) == 2
