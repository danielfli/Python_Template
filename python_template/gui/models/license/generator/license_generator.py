from utils.helper import License_Signer

# example https://pycryptodome.readthedocs.io/en/latest/src/signature/pkcs1_v1_5.html
# discription : https://pycryptodome.readthedocs.io/en/latest/src/signature/signature.html

## private key for message signing on server side
## public key for message verification on clinet side


class License_Generator:
    def __init__(
        self,
        path_public_key: str,
        path_private_key: str,
    ):
        self.path_public_key = path_public_key
        self.path_private_key = path_private_key
        self.signer = License_Signer(
            path_key_pub=self.path_public_key,
            path_key_priv=self.path_private_key,
        )

    def create_hash_from_ts(self, timestamp: str) -> str:
        self.hash = self.signer.create_hash_from_data(timestamp.encode("utf-8"))
        print("[gen] Hash created")
        return self.hash.hexdigest()

    def create_signature(self) -> bytes:
        self.signer.load_keys()
        self.signature = self.signer.sign_hash_obj(self.hash)
        print("[gen] Signature created")
        return self.signature

    def check_signature(self):
        self.signer.check_signatur(self.hash, self.signature)
