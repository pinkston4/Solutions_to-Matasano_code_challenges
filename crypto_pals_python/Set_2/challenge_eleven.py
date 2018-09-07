#! /usr/bin/env python3

# Write a function to generate a random AES key; that's just 16 random bytes.
# Write a function that encrypts data under an unknown key --- that is, 
# a function that generates a random key and encrypts under it.
# Under the hood, have the function append 5-10 bytes (count chosen randomly)
# before the plaintext and 5-10 bytes after the plaintext.
# Now, have the function choose to encrypt under ECB 1/2 the time, 
# and under CBC the other half (just use random IVs each time for CBC). Use rand(2) to decide which to use.
# Detect the block cipher mode the function is using each time. You should end up with a piece of code that, 
# pointed at a block box that might be encrypting ECB or CBC, tells you which one is happening.

import os
import sys
import string
import random
from Crypto.Cipher import AES


def pkcs_seven(message, intended_block_size):
    """
    a function that implements the PKCS#7 padding standard
    Arguments:
        message = block from the txt that should be the leng of the 
        "intended_block_size" or less long. If less then padding is implemented
        intended_block_size = intended size of the block
    """
    if (intended_block_size - len(message)) > 0:
        padding = int(intended_block_size - len(message))
    else:
        padding = 0
    assert 0 <= padding <= 255
    actual_padding = chr(padding) * padding
    block = message + bytes(actual_padding, encoding='ascii')
    return block


def random_bytes(keysize):
    """
    Arguments: 
        keysize = the desired length (in bytes) of the random string of bytes
    Returns: 
        a random string of bytes of the desired length
    """
    key = ''
    for j in range(keysize):
        i = chr(random.randint(0, 127))
        key += i
    return bytes(key, encoding="ascii")


def main(argv):
    """
    The encryption oracle
    Arguments:
        argv = should be a relative path to a file that you wish to encrypt
    Returns:
        a tuple containing the encrypted text along with either a 1 or a 0
        if a 1 is returned the txt was encoded under ECB mode if a 0 is returned
        the text was encoded in CBC mode
    """
    keysize = 16
    aes_key = random_bytes(keysize)
    prepend = random_bytes(random.randint(5, 10))
    append = random_bytes(random.randint(5, 10))

    try:
        path = dir_path + argv[0]
        with open(path) as inputfile:
            input = bytearray(inputfile.read(), encoding="ascii")
    except Exception as e:
        print(e)
        sys.exit(1)
    
    txt = prepend + input + append

    if random.randint(0, 1):
        aes_ecb = AES.new(aes_key, AES.MODE_ECB)
        out = bytearray()
        for j in range(0, len(txt), AES.block_size):
            block = txt[j: j + AES.block_size]
            padded = pkcs_seven(block, AES.block_size)
            out += aes_ecb.encrypt(padded)
        return (out, 1)
    else:
        init_vector = random_bytes(AES.block_size)
        aes = AES.new(key=aes_key, mode=AES.MODE_CBC, IV=init_vector)
        out = bytearray()
        for j in range(0, len(txt), AES.block_size):
            block = txt[j: j + AES.block_size]
            padded = pkcs_seven(block, AES.block_size)
            out += aes.encrypt(padded)
        return (out, 0)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(main(sys.argv[1:2]))
