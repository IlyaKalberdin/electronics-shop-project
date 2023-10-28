class InstantiateCSVError(Exception):
    """Класс-исключение для работы с поврежденным файлом item.csv"""
    def __init__(self, *args, **kwargs):
        self.message = "Файл item.csv поврежден"
