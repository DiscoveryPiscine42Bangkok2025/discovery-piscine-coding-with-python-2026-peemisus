#!/bin/env python3
def array_of_names(dict_person):
    return[f"{key.capitalize()} {values.capitalize()}"for key,values in dict_person.items()]
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
