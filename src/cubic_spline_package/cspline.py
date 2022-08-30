#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:35:07 2022

@author: rdempsey
"""


import numpy as np
import argparse
import convert_text
import cubic_spline_coeffs, cubic_spline_eval

parser = argparse.ArgumentParser(description='returns the cubic spline of set of points')

parser.add_argument('-xy',dest='xy',default=False)
parser.add_argument('-g',dest='grid',default=False)
parser.add_argument('-o',dest='out',default='out.txt')

args = parser.parse_args() 

if not args.xy: quit()

xy=convert_text.convert_text(args.xy,2)

if not args.grid: grid=xy[0]
else: grid=np.squeeze(convert_text.convert_text(args.grid,1))

x=xy[0]
y=xy[1]

(b,c,d)=cubic_spline_coeffs.cubic_spline_coeffs(x, y)
S=cubic_spline_eval.cubic_spline_eval(x,y,b,c,d,grid)

np.savetxt(args.out, S, delimiter=',')