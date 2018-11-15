#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:19:14 2018

@author: l-r-h
"""

#%%

import Utils.functions as func
import Data.triangles as tri


def area_triangles(lst):
    i = 0
    while i < len(tri.triangle_definitions):
        print (func.area_triangle(tri.triangle_definitions[i]['base'], tri.triangle_definitions[i]['height']))
        i = i+1
    else: 
        return None