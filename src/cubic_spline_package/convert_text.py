#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Converts .txt files to numpy arrays. Takes as arguments a filename and the number of vectors "n".
Takes a .txt file with commas separating successive values, and vectors separated by '\n', returns
an array of n numpy vectors. 
"""

import numpy as np

def convert_text(file,n):
    with open(file) as f:
        s=f.read()
        
    x=s.split('\n',n-1)
    vecs=[]
    for y in x:
        y=y.split(',')
        y=[''.join(d for d in i if d.isdigit() or d == '.' or d == '-' or d=='e' or d=='+') for i in y]
        y=[float(d) for d in y if d]
        y=np.array(y)
        vecs.append(y)
    
    return(np.array(vecs))