#! /usr/bin/env python3

# This is the sixth challenge of set one of the matasano crptopals code challenges
# https://cryptopals.com/sets/1/challenges/6
# There is a file that has been base64'ed after being encrypted with a repeating key xor
# Objective: Decrypt it 
# 1. Let KEYSIZE be the guessed length of the key; try values from lets say 2 to 40
# 2. Write a function to compute the edit distance/Hamming distance between two strings. 
#    The Hamming distance is just the number of differing bits. 
#    The distance between:
#    this is a test 
#    and
#    wokka wokka!!!
#    is 37. MAKE SURE YOUR CODE AGREES BEFORE YOU PROCEED
# 3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes,
#    and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
# 4. The KEYSIZE with the smallest normalized edit distance is probably the key. 
#    You could proceed perhaps with the smallest 2-3 KEYSIZE values. 
#    Or take 4 KEYSIZE blocks instead of 2 and average the distances.
# 5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
# 6. Now transpose the blocks: make a block that is the first byte of every block, 
#    and a block that is the second byte of every block, and so on.
# 7. Solve each block as if it was single-character XOR. You already have code to do this.
# 8. For each block, the single-byte XOR key that produces the best looking histogram
#    is the repeating-key XOR key byte for that block. Put them together and you have the key.
#
# This challenge definitely came with a learning curve, below is a list of resources used by me to help me through
# https://laconicwolf.com/
# https://trustedsignal.blogspot.com/2015/06/xord-play-normalized-hamming-distance.html
# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
# https://en.wikipedia.org/wiki/Hamming_distance
# 
# A MESSAGE TO MATASANO....lay off the vanilla ice, it will rot your minds faster than the drugs will


import base64
from operator import itemgetter

def repeating_key_xor(message, key):
    """
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
    """
    """
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
    a helper function for break_rep_key_xor, breaks the cipher text into chunks 
    the size of the key and stores in a python list
    Argumentes:
        ciphertxt = the ciphertxt that has been read into memory
        keysize = they current keysize
    Return: 
        blocks = a list of chunks of the cipher text with the length (in bytes) 
                 of the current keysize
    """
    blocks = []
    for i in range(0, len(ciphertxt), keysize):
        blocks.append(ciphertxt[i:i + keysize])
    return blocks


def helper_two(average_distances, ciphertxt):
    """
    I couldnt think of a better name for this function
    """
    possible_key_size = sorted(average_distances, key=itemgetter("avg_distance"))[0]
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

        # the hamming distances for each of the blocks of a given keysize
        distances = []

        #
        blocks = break_rep_key_xor_helper(ciphertxt, keysize)
        while True:
            try:

                block1 = blocks[0]
                block2 = blocks[1]

                # calculate the hamming distance
                # then normalize by dividing by keysize 
                normalized_distance = hamming_distance(block1, block2) / keysize
                distances.append(normalized_distance)

                # delete the first two elements of the blocks list, so they 
                # are not compared again
                del blocks[0:2]

            # the exception is thrown when there are not two blocks left
            # meaning the end of the ciphertxt
            # breaks out of the while loop
            except Exception:
                break
        
        # average normalized hamming distance for a specific key
        avg = sum(distances) / len(distances)
        result = {
            "key": keysize,
            "avg_distance": avg
        }
        avg_distances.append(result)
    return (helper_two(avg_distances, ciphertxt))


def hamming_distance(b1, b2):
    """
    The hamming distance function finds the number of differing bits between two inputs.
    It uses the zip function on the two inputs allowing easy comparison and a single for loop.
    Inside the for loop, the xor operator is used to find the difference and then the "1"s are 
    counted (the ones being the differing bits) and then added to the hamming distance
    Arguments:
        b1 = block1 passed by break_rep_key_xor, a chunk of the ciphertxt that is the length of
             keysize (amount of bytes not plaintext characters)
        b2 = block2 passed by break_rep_key_xor, a chunk of the ciphertxt that is the length of
             keysize (amount of bytes not plaintext characters)
    Return:
        the hamming distance between the two chunks of the ciphertext
    """
    ham_distance = 0
    for byte1, byte2 in zip(b1, b2):
        difference = byte1 ^ byte2
        c = bin(difference).count("1")
        ham_distance += c
    return ham_distance


def main():
    # open the encrypted file, decode it, read it into memory 
    with open('challenge_data.txt') as encoded_file:
        ciphertxt = base64.b64decode(encoded_file.read())
    
    # the correct key and result
    result, key = break_rep_key_xor(ciphertxt)
    print("{}".format(result))


if __name__ == "__main__":
    main()
