#!/usr/bin/env python3
import sys
if len(sys.argv) == 1:
 for i in range(11):
  print(f"Table de {i}:",end="")
  for l in range(11):
    print(f" {l*i}",end="")
  print()
else:
    print("none")

