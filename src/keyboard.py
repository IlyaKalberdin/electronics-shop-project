from src.item import Item


class MixinLanguage:
    """Миксин для хранения раскладки клавиатуры"""
    __language = "EN"

    @property
    def language(self):
        """Возвращает приватный __language"""
        return self.__language

    def change_lang(self):
        """Метод меняет раскладку (RU или EN)"""
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"


class Keyboard(Item, MixinLanguage):
    """Класс для представления клавиатуры в магазине"""
    def __init__(self, name, price, quantity):
        """Инициализация экземпляра класса"""
        super().__init__(name, price, quantity)
