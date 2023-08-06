# Напишите метод, на вход которого подаётся двумерный строковый массив размером 4х4.
# При подаче массива другого размера необходимо бросить исключение MyArraySizeException.
# Далее метод должен пройтись по всем элементам массива,
# преобразовать в int и просуммировать.
# Если в каком-то элементе массива преобразование не удалось
# (например, в ячейке лежит символ или текст вместо числа),
# должно быть брошено исключение MyArrayDataException с детализацией,
# в какой именно ячейке лежат неверные данные.
# В методе main() вызвать полученный метод,
# обработать возможные исключения MyArraySizeException
# и MyArrayDataException и вывести результат расчета
# (сумму элементов, при условии что подали на вход корректный массив).

class MyArraySizeException(Exception):
    def __init__(self, msg: str = "Размер списка не 4x4"):
        super().__init__(msg)


class MyArrayDataException(Exception):
    def __init__(self, first_index: int = None, second_index: int = None, msg: str = "Неверные данные"):
        if first_index and second_index:
            super().__init__(f"{msg} в ячейке [{first_index}][{second_index}]")
        else:
            super().__init__(msg)


def sum_2d_array_4x4(list1: list[list]):
    if len(list1) != 4:
        raise MyArraySizeException
    for i in list1:
        if not isinstance(i, list) or len(i) != 4:
            raise MyArraySizeException
        for j in i:
            if isinstance(j, list):
                raise MyArraySizeException

    sum = 0
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            try:
                sum += int(list1[i][j])
            except ValueError:
                raise MyArrayDataException(i, j)

    return sum


def main():
    list1 = [[1, 2, 3], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    list2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, "11f", 12], [13, 14, 15, 16]]
    list3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    list4 = [list1, list2, list3]
    for i in list4:
        try:
            print(sum_2d_array_4x4(i))
        except MyArraySizeException as e:
            print(e)
        except MyArrayDataException as e:
            print(e)


if __name__ == '__main__':
    main()
