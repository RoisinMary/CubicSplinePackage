#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:35:07 2022

@author: rdempsey
"""
import convert_text
import argparse
import compute_CS
import numpy as np

parser = argparse.ArgumentParser(description='returns the cubic spline of set of points')

parser.add_argument('xy')
parser.add_argument('-g',dest='grid',default=False)
parser.add_argument('-o',dest='out',default='out.txt')

args = parser.parse_args() 

xy=convert_text.convert_text(args.xy,2)

if not args.grid: grid=xy[0]
else: grid=convert_text.convert_text(args.grid,1)

S=compute_CS.CS(xy[0],xy[1],grid)

np.savetxt(args.out, S,delimiter=',')