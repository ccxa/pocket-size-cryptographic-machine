import hashlib
import base64


def encoder(data):
    # converting data to base64
    encoded_data = data.encode('utf-8')
    encoded_data = base64.b64encode(encoded_data)

    # converting encoded data to chr index
    numeric_data = ""
    for letter in encoded_data:
        numeric_data += str(int(letter) + 10000)

    return int(numeric_data)


def enc(data, secret, data_type):

    if data_type == "file":
        data = open(data, 'r').read()

    secret_hash = hashlib.sha256(
        str(secret).encode("utf-8")
    ).hexdigest()

    numeric_data = encoder(data)
    numeric_secret = encoder(secret_hash)
    output = (numeric_data * numeric_secret) * 1024


def dec(data, secret, data_type):

    if data_type == "file":
        data = open(data, 'r').read()

    secret_hash = hashlib.sha256(
        str(secret).encode("utf-8")
    ).hexdigest()
    numeric_secret = encoder(secret_hash)

    data = str(
        int(
            (int(data) // 1024) // numeric_secret
        )
    )

    encoded_data = ""
    while len(data) > 0:
        char = chr(int(data[0:5]) - 10000)
        data = data[5:]
        encoded_data += char

    output = base64.b64decode(encoded_data)
    output = output.decode('utf-8')
    print(output)

