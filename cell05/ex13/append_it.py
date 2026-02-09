#!/bin/env python3
import sys
if (len(sys.argv)==1):
 print("none")  
else:
    for i in sys.argv[1:]:
     if(i.lower().endswith("ism")):
        continue
     else:
        print(i+"ism")
 
 
