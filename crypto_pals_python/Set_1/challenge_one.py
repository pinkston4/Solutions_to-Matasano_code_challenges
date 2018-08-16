#! /usr/bin/env python3

"""
This is the first challenge in set one of the Matasano Cryptopals code
challenges.The challenge is to take a hexidecimal string and convert
it to a base64 string.
The string: 
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
The result:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
"""
import codecs
import unittest

class Test_conversion(unittest.TestCase):
    """
    Test_conversion is a test case that has one method test_converter
    checks to see if the given input by cryptopals matches the expected output
    """
    def test_converter(self):
        a = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        b = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        c = Hex_to_BaseSF(a)
        self.assertEqual(c.converter(), b)


class Hex_to_BaseSF:
    """
    Hex_to_BaseSF is a class with one attribute and one method, the attribute
    is the input string the method converts it from base16 to base64 and
    returns the base64 string
    """
    def __init__(self, input_hex):
        self.a = input_hex
    
    def converter(self):
        """
        The line of code below actually does whole job. No need for a class or
        additional methods. replace self.a with the hex string and the below
        line of code does everthing
        """
        b64 = codecs.encode(codecs.decode(self.a, 'hex'), 'base64').decode().replace('\n', '')
        return(b64)

    
if __name__ == "__main__":
    print("This is a script to take a string input that is hexidecimal and convert in to base64")
    input_string = input("Enter the HEX string then press Enter:")
    h_to_b64 = Hex_to_BaseSF(input_string).converter()
    print('\n\n The hex string converted to base64 is {0}'.format(h_to_b64))

