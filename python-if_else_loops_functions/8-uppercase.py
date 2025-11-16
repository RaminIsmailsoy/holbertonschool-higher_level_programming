#!/usr/bin/python3
ef uppercase(str):
    for ch in str:
        if 96 < ord(ch) < 123:
            ch = chr(ord(ch) - 32)
        print("{}".format(ch), end='')
    print()
