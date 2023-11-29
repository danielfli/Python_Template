import array

import os


# business_secret = array.array("u", ["Hello World", "76895467"])

# business_secret = array.array("B", [10, 20, 30, 40, 50])

class Store_DB:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = array.array("d")

    def load(self):
        if not os.path.exists(self.file_path):
              raise Exception("File does not exist - please call the SUPPORT TEAM")

        with open(self.file_path, "rb") as file:
            self.data.frombytes(file.read())

    def save(self):
        with open(self.file_path, "wb") as file:
            file.write(self.data.tobytes())

    def add(self, value):
        self.data.append(value)

    def remove(self, value):
        self.data.remove(value)

    def get_data(self):
        return self.data.tolist()

    def __str__(self):
        return str(self.data.tolist())

    def __repr__(self):
        return str(self.data.tolist())
