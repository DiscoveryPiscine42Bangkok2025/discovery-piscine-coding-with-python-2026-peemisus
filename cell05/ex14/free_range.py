#!/bin/env python3
import sys
if (len(sys.argv)==3):
    num1= int(sys.argv[1])
    num2= int(sys.argv[2])
    greater_num = max(num1,num2)
    fewer_num = min(num1,num2)
    startnum = fewer_num
    ranged_array = [startnum+i for i in range(greater_num-fewer_num+1)]
    print(ranged_array)
else:
 print("none")
 
