#! /usr/bin/env python3

# Set 1 challenge 7
# The Base64-encoded content in the challenge_data.txt file
# has been encrypted via AES-128 in ECB mode under the key
# "YELLOW SUBMARINE"
# (case-sensitive, without the quotes; exactly 16 characters;
# I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).
# Decrypt it. You know the key, after all.
# Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.

# nah pycrypto was easier for sure



import base64
from Crypto.Cipher import AES

def main():
    with open("challenge_data.txt") as encoded_file:
        ciphertxt = base64.b64decode(encoded_file.read())
    key = "YELLOW SUBMARINE"
    decipher = AES.new(key, AES.MODE_ECB)
    plaintext = decipher.decrypt(ciphertxt)
    print(plaintext)

if __name__ == "__main__":
    main()
