# Problem 4 - Program that encrypts the message using Caesar's cipher.

import sys
from cs50 import get_string

# check if the user do not enter key
if (len(sys.argv) != 2):
    print("Usage: python caesar.py key")
    exit(1)

# int converts string (key) to integer
key = int(sys.argv[1])

# prompt the user to enter the plaintext to be encrypted
plaintext = get_string("Plaintext: ")

# prints the encrypted ciphertext characters
print("ciphertext: ", end="")

# converts plaintext to cipertext
for c in plaintext:
    if c.isupper():
        print(chr((ord(c) - ord('A') + key) % 26 + ord('A')), end="")
    elif c.islower():
        print(chr((ord(c) - ord('a') + key) % 26 + ord('a')), end="")
    else:
        print(c, end="")
print()
