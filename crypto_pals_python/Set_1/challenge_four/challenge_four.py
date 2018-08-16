#! /usr/bin/env python3

from operator import itemgetter

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
    scores = []
    for byte in message.lower():
        s = character_frequency.get(chr(byte), 0)
        scores.append(s)
    return sum(scores)

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
    return sorted(messages, key=itemgetter('score'), reverse=True)[0]

def main():
    """
    """
    hex_strings = open('challenge_data.txt').read().splitlines()
    plain_text = []
    for cipher in hex_strings:
        ciphertxt = bytes.fromhex(cipher)
        plain_text.append(bruteforce(ciphertxt))
    best_score = sorted(plain_text, key=itemgetter('score'), reverse=True)[0]
    print(best_score)



if __name__ == "__main__":
    main()

