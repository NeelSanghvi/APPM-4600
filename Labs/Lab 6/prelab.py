# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:15:42 2024

@author: Neel
"""

import numpy

def driver():

    forward = lambda h: ((numpy.cos(s + h) - numpy.cos(s)) / h)
    center = lambda h: ((numpy.cos(s + h) - numpy.cos(s - h)) / (2*h))
    
    
    h = 0.01*2.**(-numpy.arange(0, 10))
    s = numpy.pi/2
    
    forwardDiff = forward(h)
    centerDiff = center(h)
    
    print(forwardDiff)
    print(centerDiff)
    


driver()
