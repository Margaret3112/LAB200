import doctest


class Product:
    def __init__(self, name: str, character: str, calories: int):
        """
        Создание и подготовка к работе объекта "Калорийность фруктов и овощей"

        :param name: Название продукта
        :param character: Вид продукта
        :param calories: Калорийность

        Примеры:
        >>> Product1 = Product('апельсин', 'фрукт', 'десять')
        Traceback (most recent call last):
        ...
        TypeError: Напишите калорийность числом
        >>> Product2 = Product('апельсин', 'фрукт', -3)
        Traceback (most recent call last):
        ...
        ValueError: Калорийность не может быть меньше или равна 0
        >>> Product3 = Product('вишня', 'ягода', 12)
        Traceback (most recent call last):
        ...
        ValueError: Напишите овощ или фрукт
        >>> Product4 = Product('апельсин', 2, 7)
        Traceback (most recent call last):
        ...
        TypeError: Напишите вид продукта верно

        """
        self.name = None
        self.check_name(name)
        self.character = None
        self.check_character(character)
        self.calories = None
        self.check_calories(calories)

    def check_name(self, name:str) ->None:
        if not isinstance(name, str):
            raise TypeError("Напишите название продукта верно")
        self.name=name

    def check_character(self, character:str) ->None:
        if not isinstance(character, str):
            raise TypeError("Напишите вид продукта верно")
        if character != 'фрукт' and character != 'овощ':
            raise ValueError("Напишите овощ или фрукт")
        self.character = character


    def check_calories(self, calories:int) -> None:
        if not isinstance(calories,int):
            raise TypeError("Напишите калорийность числом")
        if calories <= 0:
            raise ValueError("Калорийность не может быть меньше или равна 0")

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()