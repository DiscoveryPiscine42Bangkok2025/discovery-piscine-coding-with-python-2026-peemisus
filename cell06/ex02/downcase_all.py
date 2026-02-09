#!/bin/env python3
import sys
def downcase_it(text):
    lower_text = text.lower()
    return lower_text

if(len(sys.argv)<=1):
    print("none")
else:
    for i in sys.argv:
        print(downcase_it(i))