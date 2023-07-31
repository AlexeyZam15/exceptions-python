def main():
    # name: str = None
    # print(len(name))

    # number: str = "123fq"
    # result: int = int(number)
    # print(result)

    # dict1: dict = {1: 3, 4: 5}
    # dict1.append(object)

    # number = 1
    # try:
    #     dict1: dict = {1: 3, 4: 5}
    #     dict1.append(object)
    #     test: str = None
    #     print(len(test))
    #     number = 10 / 0
    # # except Exception:
    # #     print("Exception")
    # except ZeroDivisionError:
    #     print("operation division by zero not supported")
    # except TypeError:
    #     print("type error exception")
    # except Exception:
    #     print("Exception")
    # print(number)

    test = None
    try:
        # test = open("test")
        test = open("../.gitignore")
        test.read()
    except FileNotFoundError or EOFError as e:
        print(f"Catch exception {e.__class__.__name__}")
    finally:
        print("Finally start")
        if test is not None:
            try:
                test.close()
            except Exception:
                print(f"Exception while close")
        print("Finally finished")


if __name__ == "__main__":
    main()
