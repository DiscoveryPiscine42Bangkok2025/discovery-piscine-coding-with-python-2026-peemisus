#!/usr/bin/env python3 
num = float(input("Give me a number: "))
if(num%1!=0):
 print(int((num-num%1)+1))
else:
    print(int(num))