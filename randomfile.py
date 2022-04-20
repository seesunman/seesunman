#!/usr/bin/python3
import random
import string
with open("pythonfile.txt", "a+") as f:
    for i in range(10000):
        a = random.sample(string.punctuation+string.ascii_letters,k=50)
        passwd = ''.join(a)
        f.write(f"{passwd}\n")
        passwd = ''
