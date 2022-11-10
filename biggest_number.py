#!/usr/bin/env python

num1 = int(input("Enter a Number1 : "))
num2 = int(input("Enter a Number2 : "))
num3 = int(input("Enter a Number3 : "))
if (num1 >= num2) and (num1 >= num3):
   Max = num1
elif (num2 >= num1) and (num2 >= num3):
   Max = num2
else:
   Max = num3
print("Max Is", Max)
