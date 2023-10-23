from src.keyboard import Keyboard
import pytest


@pytest.fixture
def test_data():
    """Возвращает тестовые данные"""
    return Keyboard("Клавиатура", 10000, 10)


def test_Keyboard(test_data):
    """Тест атрибутов класса Keyboard"""
    assert test_data.name == "Клавиатура"
    assert test_data.price == 10000
    assert test_data.quantity == 10
    assert test_data.language == "EN"


def test_mixin_change_lang(test_data):
    """Тест метода change_lang миксина MixinLanguage"""
    test_data.change_lang()
    assert test_data.language == "RU"

    test_data.change_lang()
    assert test_data.language == "EN"
