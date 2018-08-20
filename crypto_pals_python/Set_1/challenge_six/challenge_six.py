#! /usr/bin/env python3

import base64

# def get_score(message):
#     """
#     coverts characters of message to lower case
#     iterates over the bytes and gets the frequency of each character
#     that it represents, if the character is not in character_frequency
#     dictionary than s = 0
#     Arguments:
#         message = the hex string that has been converted to raw bytes and 
#         xor'ed against the key of an ascii character
#     returns: sum of all scores
#     """
#     # character frequency table from Robert Lewand Cryptological Mathematics, pg. 36
#     character_frequency = {
#         'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
#         'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
#         'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
#         'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
#         'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
#         'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
#         'y': .01974, 'z': .00074, ' ': .13000
#     }
#     scores = []
#     for byte in message.lower():
#         s = character_frequency.get(chr(byte), 0)
#         scores.append(s)
#     return sum(scores)

# def repeating_key_xor(message, key):
#     """
#     Arguments:
#         message = the byte literal of the opening stanza of the..trolltrollltroll
#         key = the byte literal of the encryption key 'ICE'
#     return: 
#         the byte literal of the encrypted string
#     """
#     output = b''

#     # the current index of repeating key character
#     key_index = 0
#     # iterate over the bytes of byte literal of the.. trolltrolltroll
#     for byte in message:
#         # XOR byte and single character of repeating key 
#         output += bytes([byte ^ key[key_index]])
#         # check position of index, if end of key is reached, set index to 0 and
#         # repeat
#         if (key_index + 1) == len(key):
#             key_index = 0
#         else:
#             key_index += 1
#     return output

# def xor(a, b):
#     z = bytearray(len(a))
#     for i in range(len(a)):
#         z[i] = a[i] ^ b[i]
#     return(z)

def hamming_distance():
    pass

def main():
    with open('challenge_data.txt') as encoded_file:
        ciphertxt = base64.b64decode(encoded_file.read())

if __name__ == "__main__":
    main()    
