from ast import Bytes
import os

import binascii

from numpy import byte

class Store_DB:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = bytearray()

    def load(self):
        if not os.path.exists(self.file_path):
            raise Exception(
                "File does not exist - please call the SUPPORT TEAM"
            )

        with open(self.file_path, "rb") as file:
            self.data = file.read()

    def save(self):
        with open(self.file_path, "wb") as file:
            file.write(self.data)

    def add(self, value):
        self.data += value

    def get_data(self):
        return binascii.unhexlify(self.data).decode("ascii")


class TranslateLicense:
    def __init__(self, data: str = ""):
        self.data = data
        self.seperator = "||"
        self.array = []

    def translate(self):
        self.array = self.data.split(self.seperator)
        return self.array

