#!C:\Users\kamtak\AppData\Local\Microsoft\WindowsApps\python.exe
import random

a = int(input('whats range ,first one :'))
b = int(input("end secend one :"))
n = 1
while n > 0:
    e = random.randint(a, b)
    print(e)
    w = input("big or not ? just tell true :")
    if w == "big":
        b = b == e

    elif w == "not":
        a = a == e

    elif w == "true":
        print("bye bye")
        break

    else:
        print("what! , read carefully and enter again :")

    n += 1
