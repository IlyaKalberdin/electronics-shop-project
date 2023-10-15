import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        """
        Возвращает значение приватного аргумента
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Функция, позволяющая поменять значение приватного аргумента
        """
        if len(name) > 10:
            print("Exception: Длина наименования товара превышает 10 символов")
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Функция, создающая экземпляры класса на основе файла items.csv
        """
        cls.all = []

        with open(path, encoding="cp1251") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                item = cls(row["name"], row["price"], row["quantity"])

    @staticmethod
    def string_to_number(string):
        """
        Функция преобразует str в int и возвращает значение
        """
        return int(float(string))
