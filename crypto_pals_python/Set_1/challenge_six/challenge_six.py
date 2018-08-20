#! /usr/bin/env python3

import base64
from operator import itemgetter

def repeating_key_xor(message, key):
    """
    Arguments:
        message = the byte literal of the opening stanza of the..trolltrollltroll
        key = the byte literal of the encryption key 'ICE'
    return: 
        the byte literal of the encrypted string
    """
    output = b''

    # the current index of repeating key character
    key_index = 0
    # iterate over the bytes of byte literal of the.. trolltrolltroll
    for byte in message:
        # XOR byte and single character of repeating key 
        output += bytes([byte ^ key[key_index]])
        # check position of index, if end of key is reached, set index to 0 and
        # repeat
        if (key_index + 1) == len(key):
            key_index = 0
        else:
            key_index += 1
    return output

def xor(a, j):
    """
    """
    z = b''
    for byte in a:
        z += bytes([byte ^ j])
    return(z)


def bruteforce(cipher):
    messages = []
    # use range 256 because there are exactly 256 ascii characters
    for j in range(256):
        m = xor(cipher, j)
        s = get_score(m)
        d = {
         'message': m,
         'score': s,
         'key': j
         }
        messages.append(d)
    # print(sorted(messages, key=itemgetter('score'), reverse=True)[0])
    return sorted(messages, key=itemgetter('score'), reverse=True)[0]


def get_score(message):
    """
    coverts characters of message to lower case
    iterates over the bytes and gets the frequency of each character
    that it represents, if the character is not in character_frequency
    dictionary than s = 0
    Arguments:
        message = the hex string that has been converted to raw bytes and 
        xor'ed against the key of an ascii character
    returns: sum of all scores
    """
    # character frequency table from Robert Lewand Cryptological Mathematics, pg. 36
    character_frequency = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    scores = []
    for byte in message.lower():
        s = character_frequency.get(chr(byte), 0)
        scores.append(s)
    return sum(scores)


def break_rep_key_xor_helper(ciphertxt, keysize):
    """
    """
    blocks = []
    for i in range(0, len(ciphertxt), keysize):
        blocks.append(ciphertxt[i:i + keysize])
    return blocks

def helper_two(average_distances, ciphertxt):
    """
    """
    possible_key_size = sorted(average_distances, key=itemgetter("avg_distance"))[0]
    print(possible_key_size)
    possible_txt = []
    possible_key = possible_key_size["key"]
    key = b''
    for j in range(possible_key):
        block = b''
        for i in range(j, len(ciphertxt), possible_key):
            block += bytes([ciphertxt[i]])
        key += bytes([bruteforce(block)['key']])
    possible_txt.append((repeating_key_xor(ciphertxt, key), key)) 
    return max(possible_txt, key=lambda x: get_score(x[0])) 



def break_rep_key_xor(ciphertxt):
    """
    """
    avg_distances = []
    for keysize in range(2, 41):
        distances = []
        blocks = break_rep_key_xor_helper(ciphertxt, keysize)
        while True:
            try:
                block1 = blocks[0]
                block2 = blocks[1]
                normalized_distance = hamming_distance(block1, block2) / keysize
                distances.append(normalized_distance)
                del blocks[0:2]
            except Exception:
                break
        avg = sum(distances) / len(distances)
        result = {
            "key": keysize,
            "avg_distance": avg
        }
        avg_distances.append(result)
    return (helper_two(avg_distances, ciphertxt))

def hamming_distance(b1, b2):
    """
    """
    ham_distance = 0
    for byte1, byte2 in zip(b1, b2):
        difference = byte1 ^ byte2
        c = bin(difference).count("1")
        ham_distance += c
    return ham_distance


def main():
    with open('challenge_data.txt') as encoded_file:
        ciphertxt = base64.b64decode(encoded_file.read())
    result, key = break_rep_key_xor(ciphertxt)
    print("Key: {}\n Message:{}".format(key, result))

if __name__ == "__main__":
    main()
