from .auth import Auth

from .license.generator.utils.helper import License_Array
from .license.generator.utils.timestamp import Timestamp
from .license.license import License

PATH_LICENSE_BIN = "license.bin"
PATH_PUBLIC_KEY = "public.pem"


class Model:
    def __init__(self):
        self.tp_now = Timestamp()
        self.license_array = License_Array(PATH_LICENSE_BIN)
        self.auth = Auth()

    def check_license(self) -> bool:
        print("current time: ", self.tp_now.get_current_time)
        try:
            self.license_array.load()
            self.license = License(self.license_array.get_data())
            secret_data_array = self.license.translate_license_array()

            self.license.check_validity(secret_data_array[1])

            self.license.verify_signature(
                PATH_PUBLIC_KEY, secret_data_array[1], secret_data_array[2]
            )

            return True
        except Exception as e:
            print(e)
            return False
