d# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:35:43 2016

@author: fruzsi
"""

import sys

def hello():
    global name
    name = "World"

  
    if len(sys.argv) == 2:
        name = sys.argv[1]

    elif len(sys.argv) > 2:
        name = sys.argv[1] + " " + sys.argv[2]

def screen():
    print("Hello " + name + "!")


hello()
screen()