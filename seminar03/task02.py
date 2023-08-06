# Создайте класс Счетчик, у которого есть метод add(),
# увеличивающий значение внутренней int переменной на 1.
# Сделайте так, чтобы с объектом такого типа можно было работать
# в блоке try-with-resources.
# Подумайте, что должно происходить при закрытии этого ресурса?
# Напишите метод для проверки, закрыт ли ресурс.
# При попытке вызвать add() у закрытого ресурса,
# должен выброситься IOException+


class Counter(object):
    def __init__(self):
        self.counter = 0
        self.closed = True

    def add(self):
        if self.closed:
            raise IOError("Счётчик закрыт")
        self.counter += 1

    def __enter__(self):
        self.closed = False
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closed = True

    def __str__(self):
        return str(self.counter)


def main():
    counter = Counter()
    print(counter)
    with counter as cnt:
        cnt.add()
    print(counter)
    counter.add()


if __name__ == '__main__':
    main()
