#! /usr/bin/python

import sys

def do_map(doc): 
    for word in doc.split(): 
        yield word.lower(), 1 

for line in sys.stdin: 
    for key, value in do_map(line): 
        print(key + '\t' + str(value))
