#!/bin/env python3
import sys
def greetings(text=None):
    name=""
    if(text==None):
     name ="noble stranger"
    elif(not isinstance(text,str)):
     print("Error! It was not a name.")
     return
    else:
     name = text
    print(f"Hello,{name}")
    
    
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(2)
