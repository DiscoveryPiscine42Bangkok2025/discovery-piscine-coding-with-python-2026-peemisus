#!/bin/env python3
import sys
def shrink(text_to_shrink):
    shrank_text = text_to_shrink[:8]
    return shrank_text
def enlarge(text_to_fill):
    filled_text = text_to_fill+("Z"*(8-len(text_to_fill)))
    return filled_text
if(len(sys.argv)<=1):
    print("none")
else:
    for i in sys.argv[1:]:
        if(len(i)>=8):
            print(shrink(i))
        else:print(enlarge(i))