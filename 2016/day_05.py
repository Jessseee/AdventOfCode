# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from hashlib import md5

from aoc.helpers import *

if __name__ == "__main__":
    input = import_input("\n", example=False)[0]
    password = ["_"] * 8
    print(f"\r{''.join(password)}", end="")

    i = 0
    while "_" in password:
        bstr = bytes(f"{input}{i}", "utf-8")
        h = str(md5(bstr).hexdigest())
        i += 1
        if h.startswith("00000"):
            if h[5].isnumeric() and int(h[5]) < 8 and password[int(h[5])] == "_":
                password[int(h[5])] = h[6]
                print(f"\r{''.join(password)}", end="")
