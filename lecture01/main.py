import os


def get_file_size(file_path: str):
    if not os.path.exists(file_path):
        return -1
    return os.path.getsize(file_path)


def divide_old(a1: int, a2: int):
    if a2 == 0:
        return -1
    return a1 / a2


def a():
    b()


def b():
    c()


def c():
    ints = list[int]()
    print(ints[1000])


def divide(a1: int, a2: int):
    if a2 == 0:
        raise RuntimeError("Divide by zero not permitted")
    return a1 / a2


def main():
    # print(get_file_size("task02.py"))
    # print(get_file_size("1.py"))

    # print(divide_old(-10, 0))
    # print(divide_old(-10, 10))

    # a()

    print(divide(10, 0))


if __name__ == "__main__":
    main()
