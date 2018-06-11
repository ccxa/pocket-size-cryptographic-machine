import hashlib
import base64

import ui


def numerical_encoder(data):
    # converting data to base64
    encoded_data = data.encode('utf-8')
    encoded_data = base64.b64encode(encoded_data)

    # converting encoded data to ascii chr index
    numeric_data = ""
    for letter in encoded_data:
        # Equalize lengths ie: 95, 105 >> 10095, 10105
        numeric_data += str(int(letter) + 10000)

    return int(numeric_data)


def enc(data, secret, data_type):

    if data_type == "file":
        try:
            data = open(data, 'r').read()
        except IOError:
            ui.print_colorful("File not found!", 'red')
            return None

    secret_hash = hashlib.sha256(
        str(secret).encode("utf-8")
    ).hexdigest()
    print(data)
    numeric_data = numerical_encoder(data)
    numeric_secret = numerical_encoder(secret_hash[0:6])
    encrypted_data = (numeric_data * numeric_secret) * 102

    print(encrypted_data)


def dec(data, secret, data_type):

    if data_type == "file":
        try:
            data = open(data, 'r').read()
        except IOError:
            ui.print_colorful("File not found!", "red")

    # making secret ready for decryption
    secret_hash = hashlib.sha256(
        str(secret).encode("utf-8")
    ).hexdigest()
    numeric_secret = numerical_encoder(secret_hash[0:6])

    # main process of decryption
    numeric_data = str(
        int(
            (int(data) // 102) // numeric_secret
        )
    )

    # converting decrypted numeric data to base64 string
    base64_str = ""
    while len(numeric_data) > 0:
        # We divide numeric data into five-digit groups
        # Subtract 10000 from each batch: just reverse of line 14
        char = chr(int(numeric_data[0:5]) - 10000)
        numeric_data = numeric_data[5:]
        base64_str += char

    readable_str = base64.b64decode(base64_str)
    readable_str = readable_str.decode('utf-8')
    print(readable_str)
