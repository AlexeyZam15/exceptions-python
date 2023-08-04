from datetime import datetime


class SavedException(IOError):
    def __init__(self, msg: str, start_date: datetime, e: Exception):
        self.start_date = start_date
        super().__init__(msg, e)
