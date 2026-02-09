#!/bin/env python3
first_array = [2, 8, 9, 48, 8, 22, -12, 2]
print(first_array)
new_array = [i + 2 for i in first_array if i>5]
new_set = set(new_array)
print(new_set)