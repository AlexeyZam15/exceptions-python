# Создайте метод doSomething(),
# который может быть источником одного из типов checked exceptions
# (тело самого метода прописывать не обязательно).
# Вызовите этот метод из main и обработайте в нем исключение,
# которое вызвал метод doSomething().

def do_something():
    raise Exception


def main():
    try:
        do_something()
    except Exception:
        print("Исключение Exception")


if __name__ == "__main__":
    main()
