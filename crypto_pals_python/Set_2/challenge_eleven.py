#! /usr/bin/env python3

# Write a function to generate a random AES key; that's just 16 random bytes.
# Write a function that encrypts data under an unknown key --- that is, 
# a function that generates a random key and encrypts under it.
# Under the hood, have the function append 5-10 bytes (count chosen randomly)
#  before the plaintext and 5-10 bytes after the plaintext.
# Now, have the function choose to encrypt under ECB 1/2 the time, 
# and under CBC the other half (just use random IVs each time for CBC). Use rand(2) to decide which to use.
# Detect the block cipher mode the function is using each time. You should end up with a piece of code that, 
# pointed at a block box that might be encrypting ECB or CBC, tells you which one is happening.

import string
import random
from Crypto.Cipher import AES

def build_key():
    keysize = 16
    key = ''
    for j in range(keysize):
        key += random.choice(string.ascii_letters)
    key = bytes(key, encoding='ascii')
    assert keysize == len(key)
    return key

def main():
    aes_key = build_key()
    

if __name__ == "__main__":
    main()
