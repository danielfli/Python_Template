import os
import binascii

from Crypto.PublicKey import RSA

# from Crypto.Signature import PKCS1_v1_5
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# from Crypto.Signature import pkcs1_15


class ConvertStringToAscii:
    def __init__(self):
        pass

    def convert_string(self, string: str):
        return binascii.hexlify(string.encode("ascii"))

    def convert_bytes(self, data: bytes):
        return binascii.hexlify(data)


class License_Array:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = bytearray()

    def save(self):
        with open(self.file_path, "wb") as file:
            file.write(self.data)
        print("data saved to: ", self.file_path)

    def add(self, value):
        self.data += value

    def get_raw_data(self):
        print("array size ", self.data.__sizeof__())
        return self.data

    def load(self):
        if not os.path.exists(self.file_path):
            raise Exception(
                "File does not exist - please call the SUPPORT TEAM"
            )

        with open(self.file_path, "rb") as file:
            self.data = file.read()

    def get_data(self) -> bytes:
        return binascii.unhexlify(self.data)


class License_Signer:
    def __init__(
        self,
        data_msg: bytes = b"",
        path_key_pub: str = "",
        path_key_priv: str = "",
    ):
        self.data_msg = data_msg
        self.path_key_pub = path_key_pub
        self.path_key_priv = path_key_priv

    def generate_keys(self) -> None:
        key = RSA.generate(1024)
        private_key = key.export_key()
        file_out = open(self.path_key_priv, "wb")  # "prvate.pem"
        file_out.write(private_key)

        public_key = key.publickey().export_key()
        file_out = open(self.path_key_pub, "wb")  # "public.pem"
        file_out.write(public_key)

    def load_keys(self):
        if not os.path.exists(self.path_key_pub) and not os.path.exists(
            self.path_key_priv
        ):
            raise Exception("Could not finde keys - use generate_keys() first ")

        with open(self.path_key_pub, "rb") as file:
            self.key_pub = RSA.import_key(file.read())

        with open(self.path_key_priv, "rb") as file:
            self.key_priv = RSA.import_key(file.read())

    def set_data_msg(self, data_msg: bytes):
        self.data_msg = data_msg

    def create_hash_from_data(self, data_msg: bytes):
        """Signing a message with RSA

        Args:
            data_msg (bytes): Message to sign

        Returns:
            _type_: hash of SHA256
        """
        hash = SHA256.new()
        hash.update(data_msg)
        return hash

    def sign_hash_obj(self, msg_hash) -> bytes:
        """Generate a signature of the message

        Args:
            hash (SHA256Hash): hash of this message

        Returns:
            _type_: signature of the message
        """
        signatur = pkcs1_15.new(self.key_priv).sign(msg_hash=msg_hash)
        # signatur = PKCS1_v1_5.new(self.key_priv).sign(hash) old way
        return signatur

    def check_signatur(self, hash, signatur: bytes):
        try:
            pkcs1_15.new(self.key_pub).verify(hash, signatur)
            print("The signature is valid.")
        except (ValueError, TypeError):
            print("The signature is not valid.")
            exit(1)
