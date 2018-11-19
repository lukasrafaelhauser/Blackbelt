#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:05:26 2018

@author: l-r-h
"""

from Homework_2 import checkout

def test_checkout_returns():
    assert checkout(2,3,4) == 2055
    assert checkout(0,0,0) == "Thank you, bye"
    assert checkout(-4,-5, -6) == "Negative Amounts of Products are not possible"
    assert checkout(1,0,0) == 1000

#%%

from Homework_2 import checkout_advanced

y = 1
n = 0

def test_checkout_advanced():
    assert checkout_advanced(1,0,0,y,y) == 1015
    assert checkout_advanced(0,0,0,y,y) == "Thank you, bye"
    assert checkout_advanced(1,0,0,n,n) == 1000
    assert checkout_advanced(-4,0,-1,y,y) == "Negative Amounts of Products are not possible"

#%%
    
from Homework_2 import checkout_tiers

normal = 0
silver = 1
gold = 2

def test_checkout_tiers():
    assert checkout_tiers(silver,5,6,7,y,y) == 5013
    assert checkout_tiers(normal,1,0,0,n,n) == 1000
    assert checkout_tiers(gold,1,0,0,n,y) == 959.5
    assert checkout_tiers(gold,0,0,0,y,y) == "Thank you, bye"
    assert checkout_tiers(gold, -2, -2, -2 , n,y) == "Negative Amounts of Products are not possible"