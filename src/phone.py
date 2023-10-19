from src.item import Item


class Phone(Item):
    """
    Класс для представления телефона в магазине.
    """
    def __init__(self, name, price, quantity, number_of_sim):
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Функция возвращает название класса и все аргументы экземпляра
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Возврвщает значение приватного аргумента _number_of_sim
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if new_number_of_sim > 0 and isinstance(new_number_of_sim, int):
            self.__number_of_sim = new_number_of_sim
        else:
            print("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
