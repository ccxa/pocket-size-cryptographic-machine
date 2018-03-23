import values
from ui import *
import os
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

    numeric_data = encoder(data)
    numeric_secret = encoder(secret)

    output = (numeric_data * numeric_secret) * 10244
    print(output)



