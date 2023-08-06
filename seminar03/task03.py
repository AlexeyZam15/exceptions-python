# Создайте класс исключения,
# который будет выбрасываться при делении на 0.
# Исключение должно отображать понятное для пользователя сообщение об ошибке.


class DividedByZeroException(ArithmeticError):
    def __init__(self, msg: str = "Деление на 0 запрещено"):
        super().__init__(msg)


# Создайте класс исключений, которое будет возникать
# при обращении к пустому элементу в массиве ссылочного типа.
# Исключение должно отображать понятное для пользователя сообщение об ошибке.
class NoneElementException(Exception):
    def __init__(self, index: int, msg: str = "Обращение к None элементу с индексом"):
        super().__init__(f"{msg}: {index}")


class NotNoneElementList:
    def __init__(self, list1: list):
        self.list1 = list1

    def __len__(self):
        return len(self.list1)

    def __getitem__(self, item):
        if not self.list1[item]:
            raise NoneElementException(item)
        return self.list1[item]


# Создайте класс исключения, которое будет возникать
# при попытке открыть несуществующий файл.
# Исключение должно отображать понятное для пользователя сообщение об ошибке.

class IOException(IOError):
    def __init__(self, path: str, msg: str = "Файл не найден"):
        super().__init__(f"{msg}: '{path}'")


def main():
    # try:
    #     a = 1 / 0
    # except ZeroDivisionError:
    #     raise DividedByZeroException

    list1 = NotNoneElementList([1, 2, None, 5])
    for i in range(len(list1)):
        print(list1[i])

    # try:
    #     open("1.txt")
    # except IOError as e:
    #     raise IOException(e.filename)


if __name__ == '__main__':
    main()
