def readable_file(filename: str):
    try:
        open(filename)
    except FileNotFoundError:
        print("Файл не найден")
        return False
    return True


def read_file(filename: str):
    if not readable_file(filename):
        return None
    dict1 = dict()
    with open(filename, encoding="utf-8", mode="r") as file:
        for i in file:
            string = i.replace("\n", "").split("=")
            dict1[string[0]] = string[1]
    return dict1


def validate_dict(dict1: dict):
    invalid_values = ""
    for i in dict1:
        value: str = dict1[i]
        if not value.isdigit():
            if value != "?":
                invalid_values += f'\n{i}->{value}'
            dict1[i] = str(len(i))
    if invalid_values:
        raise RuntimeError(f"Некорректные данные:{invalid_values}")


def write_dict_to_file(filename: str, dict1: dict):
    with open(filename, encoding="utf-8", mode="w") as file:
        for i in dict1:
            file.write(f"{i}={dict1[i]}\n")


# Реализуйте метод, который считывает данные из файла и сохраняет в двумерный массив (либо HashMap, если студенты с
# ним знакомы). В отдельном методе нужно будет пройти по структуре данных, если сохранено значение ?, заменить его на
# соответствующее число. Если на каком-то месте встречается символ, отличный от числа или ?, бросить подходящее
# исключение. Записать в тот же файл данные с замененными символами ?.
def main():
    dict1 = read_file("1.txt")
    print(*[f"{i}={dict1[i]}" for i in dict1], sep="\n", end="\n\n")
    validate_dict(dict1)
    print(*[f"{i}={dict1[i]}" for i in dict1], sep="\n")
    write_dict_to_file("2.txt", dict1)


if __name__ == "__main__":
    main()
