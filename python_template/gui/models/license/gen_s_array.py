import array


from timestamp import Timestamp


class Create_S_License:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = array.array("d")

    def save(self):
        with open(self.file_path, "wb") as file:
            file.write(self.data.tobytes())
        print("data saved to: ", self.file_path)

    def add(self, value):
        self.data.append(value)

    def get_data(self):
        return self.data.tolist()


COSTUMER_SECRET = 40000.1
PATH_FILE = ".some_data.bin"
LICENSE_DAYS = 0
LICENSE_MIN = 1

ts = Timestamp().generate_timestamp(days=LICENSE_DAYS, minutes=LICENSE_MIN)
s_array = Create_S_License(PATH_FILE)
s_array.add(COSTUMER_SECRET)
s_array.add(ts)
print("BIN ARRAY: ", s_array.get_data())
s_array.save()
