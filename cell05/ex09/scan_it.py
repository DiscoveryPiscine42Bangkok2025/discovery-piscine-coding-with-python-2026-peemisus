#!/bin/env python3
import sys
if (len(sys.argv)==3):
 word_search = sys.argv[1]
 count = sys.argv[2].lower().count(word_search)
 print(count)
else:
 print("none")