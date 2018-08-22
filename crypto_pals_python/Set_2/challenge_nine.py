#! /usr/bin/env python3

# Set 2 Challenge 9 of the Cryptopals code challenges
# Implement PKCS#7 padding
# A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext.
# But we almost never want to transform a single block; we encrypt irregularly-sized messages.
# One way we account for irregularly-sized messages is by padding,
# creating a plaintext that is an even multiple of the blocksize. 
# The most popular padding scheme is called PKCS#7.
# So: pad any block to a specific block length,
# by appending the number of bytes of padding to the end of the block.
# For instance,
# "YELLOW SUBMARINE"
# ... padded to 20 bytes would be:
# "YELLOW SUBMARINE\x04\x04\x04\x04"

def pkcs_seven(message, intended_block_size):
    if (intended_block_size - len(message)) > 0:
        padding = int(intended_block_size - len(message))
    else:
        padding = 0
    assert 0 <= padding <= 255
    actual_padding = chr(padding) * padding
    block = message + bytes(actual_padding, encoding='ascii')
    return block

def main():
    original = b"YELLOW SUBMARINE"
    print(pkcs_seven(original, 20))

if __name__ == "__main__":
    main()