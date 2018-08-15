#! /usr/bin/env python3

# the two input strings and the desired output 
input_str_a = '1c0111001f010100061a024b53535009181c'
input_str_b = '686974207468652062756c6c277320657965'
desired_output = '746865206b696420646f6e277420706c6179'


def xor(a, b):
    z = bytearray(len(a))
    for i in range(len(a)):
        z[i] = a[i] ^ b[i]
    return(z)

a = bytearray.fromhex(input_str_a)
b = bytearray.fromhex(input_str_b)
c = bytes(xor(a, b))
d = c.hex()

print('input string one:\n{0}', input_str_a)
print('input string two:\n{0}', input_str_b)
print('expected output:\n{0}', desired_output)
print('actual output:\n{0}', d)
print(c)

