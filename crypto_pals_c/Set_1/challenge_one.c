#include <stdio.h>

int main() {
    char hexstring[] = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
    char expected_out[] = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";
    int n;
    int length_of_array;
    int size_of_char = sizeof(char);
    n = sizeof(hexstring);
    length_of_array = n / size_of_char;
    printf("%s\n", hexstring);
    printf("%d\n", length_of_array);
    return 0;
}
