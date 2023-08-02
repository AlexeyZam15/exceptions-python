def sum2d(list2d: list[list[int]]):
    sum = 0
    non_numb_elems = []
    for i in list2d:
        for j in i:
            try:
                sum += int(j)
            except (ValueError, TypeError):
                non_numb_elems.append(j)
    print("Элементы неподходяшего типа: ", *non_numb_elems)
    return sum


def main():
    list2d_1 = [["a1", [2], 3], [1, 2]]
    print(sum2d(list2d_1))


if __name__ == "__main__":
    main()
