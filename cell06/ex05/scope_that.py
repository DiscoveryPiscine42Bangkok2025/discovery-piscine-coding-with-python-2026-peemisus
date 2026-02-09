#!/bin/env python3
import sys
def add_one(num):
    num +=1
    print(f"inside method value:{num}")
num = 10
add_one(num)
print(f"outside method value:{num}")