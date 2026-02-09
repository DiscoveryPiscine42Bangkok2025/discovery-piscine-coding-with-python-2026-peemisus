#!/bin/env python3
import sys
def add_one(num):
    num +=1
    print(f"inside method value:{num}")
num = 10
print(f"1_outside method value:{num}")
add_one(num)
print(f"2_outside method value:{num}")