#!/bin/env python3
def find_the_redheads(dict_fam):
    return[f"{key}"  for key in dict_fam if dict_fam[key]=="red"]
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))

