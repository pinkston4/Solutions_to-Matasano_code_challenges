#! /usr/bin/env python3

# CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages,
# despite the fact that a block cipher natively only transforms individual blocks.
# In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.
# The first plaintext block, which has no associated previous ciphertext block, 
# is added to a "fake 0th ciphertext block" called the initialization vector, or IV.
# Implement CBC mode by hand by taking the ECB function you wrote earlier, 
# making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test), 
# and using your XOR function from the previous exercise to combine them.
# The file here is intelligible (somewhat) when CBC decrypted against 
# "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)

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