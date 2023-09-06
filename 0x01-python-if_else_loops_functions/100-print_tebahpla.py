#!/usr/bin/python3

for i in range(122, 96, -2):
    letter_lower = chr(i)
    letter_upper = chr(i + ord('A') - ord('a') - 1)
    letters = f"{letter_lower}{letter_upper}"
    print(letters, end="")
