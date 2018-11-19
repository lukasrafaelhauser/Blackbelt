# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

guitar = {"Name": "Guitar", "Price": 1000}
pickbox = {"Name": "Pick Box", "Price": 5}
guitarstrings = {"Name": "Guitar Strings", "Price": 10}

products = [guitar, pickbox, guitarstrings]

def checkout(a,b,c):
    if a + b + c < 0:
        return "Negative Amounts of Products are not possible"
    elif a + b+ c == 0:
        return "Thank you, bye"
    else:
        return (a* products[0]["Price"]) + (b* products[1]["Price"]) + (c*products[2]["Price"])
#%%
        
y = 1
n = 0


def checkout_advanced(a,b,c,ins, pri):
    '''a is amount of guitars, b is amount of pickboxes c is amount of strings; for ins(urance) and pri(ority) choose y for yes or n for no'''
    
    if a + b + c < 0:
        return "Negative Amounts of Products are not possible"
    elif a + b+ c == 0:
        return "Thank you, bye"
    else:
        return (a* products[0]["Price"]) + (b* products[1]["Price"]) + (c*products[2]["Price"]) + (ins*5) + (pri*10)

#%%

normal = 0
silver = 1
gold = 2

      
def checkout_tiers(t,a,b,c,ins, pri):
    '''
    t is for customer tier: normal = 0, silver = 1, gold = 2
    a is amount of guitars, b is amount of pickboxes c is amount of strings; 
    for ins(urance) and pri(ority) choose y for yes or n for no'''
    
    if a + b + c < 0:
        return "Negative Amounts of Products are not possible"
    elif a + b+ c == 0:
        return "Thank you, bye"
    elif t == 0:
        return (a* products[0]["Price"]) + (b* products[1]["Price"]) + (c*products[2]["Price"]) + (ins*5) + (pri*10)
    elif t == 1:
        return 0.98*((a* products[0]["Price"]) + (b* products[1]["Price"]) + (c*products[2]["Price"])) + (ins*5) + (pri*10)
    elif t == 2:
        return 0.95*((a* products[0]["Price"]) + (b* products[1]["Price"]) + (c*products[2]["Price"]) + (ins*5) + (pri*10))


#%%
        
guitar = {"Name": "Guitar", "Price": 1000}
pickbox = {"Name": "Pick Box", "Price": 5}
guitarstrings = {"Name": "Guitar Strings", "Price": 10}
products = [guitar, pickbox, guitarstrings]



        