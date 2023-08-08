import os

from seminar03.homework.app import App


def main():
    app = App()
    input_mode = True
    while input_mode:
        try:
            input_mode = app.start()
        except Exception as e:
            print(e)
    print(app.data)


if __name__ == '__main__':
    main()
