from license_generator import License_Generator
from utils.helper import License_Array, ConvertStringToAscii, License_Signer
from utils.timestamp import Timestamp

# ToDo: file to store license where?

secret_dict = {
    "path_private_key": "private.pem",
    "path_public_key": "public.pem",
    "path_bin_file": "license.bin",
    "costumer_number": "40000.1",
    "license_days": 0,
    "license_minutes": 2,
}


def Genearte_Pub_Priv_Key():
    print("Do you want to generate new keys? (y/n)")
    answer = input()
    if answer == "y":
        License_Signer().generate_keys()
        print("Keys generated")
        exit()


def Generate_License():
    license_ts = Timestamp().generate_timestamp(
        days=secret_dict["license_days"], minutes=secret_dict["license_minutes"]
    )
    license_ts_str = str(license_ts)
    print("License Timestamp: ", license_ts)

    # Hash und Signatur erstellen
    license_gen = License_Generator(
        secret_dict["path_public_key"], secret_dict["path_private_key"]
    )

    # Create Array for license
    costumer_nummer_asci = ConvertStringToAscii().convert_string(secret_dict["costumer_number"])
    license_ts_asci = ConvertStringToAscii().convert_string(license_ts_str)
    hash_str = license_gen.create_hash_from_ts(license_ts_str)
    signature_byte = license_gen.create_signature()
    signature_asci = ConvertStringToAscii().convert_bytes(signature_byte)


    license_gen.check_signature()

    # print("signature in byte: ", signature_byte)
    # print("signature in asci: ", signature_asci)
    # print("\ncostumer_nummer_asci: ", costumer_nummer_asci)
    # print("timestamp in asci: ", license_ts_asci)
    # print("timestamp in str: ", license_ts_str)

    seperator = ConvertStringToAscii().convert_string("||")
    s_array = License_Array(secret_dict["path_bin_file"])
    s_array.add(costumer_nummer_asci)
    s_array.add(seperator)
    s_array.add(license_ts_asci)
    s_array.add(seperator)
    s_array.add(signature_asci)

    print("BIN ARRAY: ", s_array.get_raw_data())

    s_array.save()

    return s_array


def main():
    # Genearte_Pub_Priv_Key()
    Generate_License()


if __name__ == "__main__":
    main()
