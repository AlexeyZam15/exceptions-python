def check_list_size(list1: list, min_size: int):
    if len(list1) < min_size:
        return -1
    return len(list1)


def list_find(list1: list, value, min_size: int, print_msg=True):
    err_str_dict = {-3: "Вместо списка находится объект None",
                    -2: "Элемент не найден",
                    -1: "Размер списка не соответствует заданному минимальному размеру списка",
                    0: "Индекс элемента ="
                    }
    code = None
    if list1 is None:
        code = -3
    if not code:
        size = check_list_size(list1, min_size)
        if size == -1:
            code = -1
        else:
            for i in range(len(list1)):
                if list1[i] == value:
                    code = i
            if not code:
                code = -2
    if print_msg:
        print_err_code(code, err_str_dict)
    return code


def print_err_code(error_code: int, err_str_dict: dict):
    if error_code in err_str_dict:
        return print(err_str_dict[error_code])
    return print(f"{err_str_dict[0]} {error_code}")


def check_is_square_2d_list(list1: list[list]):
    for i in list1:
        if len(list1) != len(i):
            return False
    return True


def check_type_2d_list(list1: list[list], list1_type1: str, nested_list_type2: str, element_type: str):
    if not str(type(list1)) == list1_type1:
        return False
    for i in list1:
        if not str(type(i)) == nested_list_type2:
            return False
        for j in i:
            if not str(type(j)) == element_type:
                return False
    return True


def sum_2d_list_elements(list1: list[list[int]]):
    sum1 = 0

    if not check_type_2d_list(list1, "<class 'list'>", "<class 'list'>", "<class 'int'>"):
        raise RuntimeError("Список имеет неверный тип данных")

    if not check_is_square_2d_list(list1):
        raise RuntimeError("Двумерный список не является квадратным")

    for i in list1:
        for j in i:
            if j not in (0, 1):
                raise RuntimeError("Значение элемента двумерного списка не равно 0 или 1")
            sum1 += j
    return sum1


def check_array(list1: list[int]):
    none_elements_indexes = []
    for i in range(len(list1)):
        if list1[i] is None:
            none_elements_indexes.append(str(i))
    if none_elements_indexes:
        raise RuntimeError(f"Список содержит нулевые элементы под индексами: "
                           f"{', '.join(none_elements_indexes)}")
    print("Нулевых элементов в списке не обнаружено")


def main():
    # list1 = [1, 2, 3, 4, 5]

    # print(check_list_size(list1, 2))

    # list_find(None, 3, 3)
    # list_find(list1, 3, 6)
    # list_find(list1, 6, 5)
    # list_find(list1, 3, 5)

    # list2d_1 = [[0, 2], [4, 5, 6]]
    # print(sum_2d_list_elements(list2d_1))
    # list2d_2 = [[0, 2], [4, 5]]
    # print(sum_2d_list_elements(list2d_2))
    # list2d_3 = [[0, 1, 1], [1, 0, 1], [1, 0, 1]]
    # print(sum_2d_list_elements(list2d_3))

    list2 = [0, 1, 3]
    check_array(list2)
    list2 = [None, 1, None]
    check_array(list2)


if __name__ == "__main__":
    main()
