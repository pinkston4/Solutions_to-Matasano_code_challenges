#! /usr/bin/env python3

"""
Challenge 5 of the CryptoPals challenges
objective: Take the opening stanza of 'ICE ICE BABY' 
by Vanilla Ice, dubbed an important work of English Literature
by the creators of the challenge...trolltrolltroll... and encrypt 
it using a repeating key xor
"""

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

def main():

    # string to be encrypted, coverted to byte literal
    message = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    # targe output
    desired_output = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272\
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    
    # the repeating key
    key = b'ICE'

    # actual output
    ciphertxt = repeating_key_xor(message, key).hex()

    # assert that the encrypted ciphertext is equal to the desired output
    assert(ciphertxt == desired_output)
    print(ciphertxt)


if __name__ == '__main__':
    main()
