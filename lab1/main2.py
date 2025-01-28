import doctest


class Survey:
    def __init__(self, gender: str, age: int):
        """
        Создание и подготовка к работе объекта "Результаты опроса"

        :param gender: Пол
        :param age: Возраст

        Примеры:
        >>> Survey1 = Survey('женщина', 'двадцать')
        Traceback (most recent call last):
        ...
        TypeError: Напишите возраст числом
        >>> Survey2 = Survey('женщина', 31)
        Traceback (most recent call last):
        ...
        ValueError: Опрос проводится в возрастной группе от 20 до 30 лет
        >>> Survey = Survey(4, 23)
        Traceback (most recent call last):
        ...
        TypeError: Напишите пол буквами

        """
        self.gender = None
        self.check_gender(gender)
        self.age = None
        self.check_age(age)

    def check_gender(self, gender:str) ->None:
        if not isinstance(gender, str):
            raise TypeError("Напишите пол буквами")
        self.gender=gender

    def check_age(self, age:int) -> None:
        if not isinstance(age,int):
            raise TypeError("Напишите возраст числом")
        if age <= 20 or age >= 30:
            raise ValueError("Опрос проводится в возрастной группе от 20 до 30 лет")

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()