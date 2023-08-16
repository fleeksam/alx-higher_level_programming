#!/usr/bin/python3
# Author - Rosemary Nwodo

i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
