def main():
    # try:
    #     # with open("test") as test:
    #     with open("../.gitignore") as test:
    #         test.read()
    # except FileNotFoundError or EOFError as e:
    #     print(f"Catch exception {e.__class__.__name__}")

    try:
        with open("../.gitignore") as reader, open("test.txt", mode="w") as writer:
            writer.write(reader.read())
    except FileNotFoundError or EOFError as e:
        print(f"Catch exception {e.__class__.__name__}")
    print("Copy successfully")


if __name__ == "__main__":
    main()
