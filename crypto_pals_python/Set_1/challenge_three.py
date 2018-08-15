#! /usr/bin/env python3

"""
Given a hex encoded input string that has been XOR'ed against a single
character, you must find the key and decrypt the cipher. This is a simple ceasar cipher.
It is entirely possible to do this by hand, but where is the fun in that.
"""
from operator import itemgetter

# input string provided by cryptopals
input_string = '1b37373331363f78151b7f2b783431333d78397828372d36\
                3c78373e783a393b3736'

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
    xor the hex string(that has been converted to bytes) against 
    a single ascii character
    return: byte literal
    """
    z = b''
    for byte in a:
        z += bytes([byte ^ j])
    return(z)

def main():
    """
    the main loop for the program
    converts hex string to bytes object
    declares empty list called messages
    iterates over key values of ascii
    j = key
    m = byte liter, possible solution
    s = score of m
    d = data/dictionary, of message score and key
    d it appended to messages at the end of every iteration
    messages are then sorted based on highest score and the message with the
    highest score is displayed, this being the answer
    """
    hex_string = bytes.fromhex(input_string)
    messages = []
    # use range 256 because there are exactly 256 ascii characters
    for j in range(256):
        m = xor(hex_string, j)
        s = get_score(m)
        d = {
         'message': m,
         'score': s,
         'key': j
         }
        messages.append(d)
        # uncomment the print statemtn and each potential message, its score,
        # and the key all print, one blog (laconic wolf) described this as a 
        # bit of visual grep, scroll do key 88 and you will see what I mean
        # print('{0}\n', d)
    answer = sorted(messages, key=itemgetter('score'), reverse=True)[0]
    print(answer)


if __name__ == "__main__":
    main()


