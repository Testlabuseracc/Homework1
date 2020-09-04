# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 01:51:18 2020

@author: Main
"""


_score = int(input("Enter number between 80 and 100: "))
if (95<= _score<=100):
    print("A+")
elif 90<=_score<95:
    print("A")
elif 85<=_score<90:
    print("A-")
elif 80<= _score<85:
    print("B+")
else:
    print("the number entered is out of range")
        
        

