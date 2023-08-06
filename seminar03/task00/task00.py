def rw_line(path_read: str, path_write: str):
    in_file = None
    out_file = None
    try:
        in_file = open(path_read, mode="r")
        out_file = open(path_write, mode="w")
        out_file.write(in_file.readline())
    except IOError:
        print("Файл не найден")
    finally:
        try:
            if in_file is not None:
                in_file.close()
        except IOError:
            pass
        try:
            if out_file is not None:
                out_file.close()
        except IOError:
            pass


def rw_line_with(path_read: str, path_write: str):
    try:
        with open(path_read, mode="r") as in_file:
            with open(path_write, mode="w") as out_file:
                out_file.write(in_file.readline())
    except IOError:
        print("Файл не найден")


def main():
    path_read = "1.txt"
    path_write = "2.txt"

    # rw_line(path_read, path_write)

    rw_line_with(path_read, path_write)


if __name__ == "__main__":
    main()
