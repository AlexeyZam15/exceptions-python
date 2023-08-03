import traceback


class SaveService:
    def save(self):
        print("save document started...")
        with open("test.txt", mode="w") as writer:
            raise IOError("operation failed")
        # try:
        #     with open("test.txt", mode="w") as writer:
        #         raise IOError("operation failed")
                # raise Exception("operation failed")
        # except IOError:
        #     traceback.print_exc()
        # except Exception as e:
        #     raise RuntimeError(e)
        # except IOError as e:
        #     raise RuntimeError(e)


if __name__ == "__main__":
    SaveService().save()
