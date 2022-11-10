#!C:\Users\kamtak\AppData\Local\Microsoft\WindowsApps\python.exe
import random

javab = random.randint (1, 99)
get = int(input("gauss the number :"))
n=1
while (n>0) :
    if get == javab :
        print("wow you have right gauss")
        break
    if get > javab :
        print("ok , its big ")
        get = int(input("again ="))

    if get < javab :
        print("higher , come on ")
        get = int(input("agian ="))
        
    n += 1


