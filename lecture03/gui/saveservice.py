import traceback

from lecture03.gui.savedexception import SavedException
from datetime import datetime


class SaveService:
    def save(self):
        date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        print("save document started...")
        # with open("test.txt", mode="w") as writer:
        #     raise IOError("operation failed")
        try:
            with open("test.txt", mode="w") as writer:
                raise IOError("operation failed")
                # raise Exception("operation failed")
        # except IOError:
        #     traceback.print_exc()
        # except Exception as e:
        #     raise RuntimeError(e)
        except IOError as e:
            raise SavedException("Saved document failed", date, e)

if __name__ == "__main__":
    SaveService().save()
