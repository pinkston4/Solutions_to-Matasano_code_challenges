#! /usr/bin/env python3


import base64
from Crypto.Cipher import AES


def cbc_decrypt(cipher, key, init_vector, block_size):
    aes = AES.new(key=key, mode=AES.MODE_CBC, IV=init_vector)
    out = aes.decrypt(cipher)
    return out

def main():
    block_size = 16
    key = b"YELLOW SUBMARINE"
    init_vector = bytes(("\00" * block_size), encoding="ascii")
    with open("challenge_data.txt") as data:
        cipher = base64.b64decode(data.read())
        print(cbc_decrypt(cipher, key, init_vector, block_size))


if __name__ == "__main__":
    main()