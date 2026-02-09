#!/bin/env python3
import sys
if (len(sys.argv)<3):
 print("none")
else:
 reverse_argv=sys.argv[1:][::-1]
 for i in reverse_argv:
  print(i)
 