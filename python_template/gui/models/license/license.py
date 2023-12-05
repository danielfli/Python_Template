from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

# from Crypto.Signature import PKCS1_v1_5
from .generator.utils.timestamp import Timestamp


import os


class License:
    def __init__(self, data: bytes):
        self.data = data
        self.seperator = "||"
        self.array = []

    def translate_license_array(self):
        self.array = self.data.split(self.seperator.encode("ascii"))
        return self.array

    def open_public_key(self, path: str):
        if not os.path.exists(path):
            raise Exception("Could not finde keys - use generate_keys() first ")

        with open(path, "rb") as file:
            self.pub_key = RSA.import_key(file.read())

    def check_validity(self, timestamp: bytes):
        tp_now = Timestamp()
        ts_license = float(timestamp)
        if tp_now.get_timestamp > ts_license:
            print(
                "license expired! valid until: ",
                tp_now.return_timestamp(ts_license),
            )
            exit(0)
        else:
            print("license valid until: ", tp_now.return_timestamp(ts_license))

    def verify_signature(self, path_pbulic_key, timestamp, signature):
        # print("timestamp: ", timestamp)
        # print("signature: ", signature)
        hash = SHA256.new(timestamp)
        try:
            self.open_public_key(path_pbulic_key)
            pkcs1_15.new(self.pub_key).verify(hash, signature)
            print("The signature is valid.")
        except (ValueError, TypeError):
            print("The signature is not valid.")
            exit(1)
