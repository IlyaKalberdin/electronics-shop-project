import csv
from src.instantiatecsverror import InstantiateCSVError


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
        super().__init__()

    def __repr__(self):
        """
        Функция возвращает название класса и все аргументы экземпляра
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Функция возвращает наименование товара
        """
        return f"{self.name}"

    def __add__(self, other):
        """
        Метод складывает экземпляры класса по кол-ву товара
        и возвращает сумму
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return None

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

        try:
            with open(path, encoding="cp1251") as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    if ("name", "price", "quantity") not in row:
                        raise InstantiateCSVError

                    item = cls(row["name"], row["price"], row["quantity"])
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except InstantiateCSVError as csv_error:
            print(csv_error.message)

    @staticmethod
    def string_to_number(string):
        """
        Функция преобразует str в int и возвращает значение
        """
        return int(float(string))
