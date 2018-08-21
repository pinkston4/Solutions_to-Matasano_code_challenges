#! /usr/bin/env python3


# Set one challenge 8
# Detect AES in ECB mode
# In the challenge_data.txt file are a bunch of hex-encoded ciphertexts.
# One of them has been encrypted with ECB.
# Detect it.
# Remember that the problem with ECB is that it is stateless and deterministic;
# the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

from binascii import a2b_hex
from collections import Counter


def ecb_encoded(cipher, block_size):
    block_range = range(0, len(cipher), block_size)
    number_of_blocks = Counter(cipher[i : i + block_size] for i in block_range)
    m = number_of_blocks.most_common(1)
    if m and m[0][1] > 1:
        return True

def main():
    with open("challenge_data.txt") as hex_lines:
        lines = (l.rstrip() for l in hex_lines)
        lines = (a2b_hex(l) for l in lines)
        lines = (l for l in lines if ecb_encoded(l, 16))
        for l in lines:
            print("{}\n".format(l.hex()))
        
if __name__ == "__main__":
    main()
