# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:06:59 2024

@author: 2021n
"""


# get lgwts routine and numpy
import numpy as np;
import numpy.linalg as la;
import matplotlib.pyplot as plt
from numpy import polynomial

from scipy import integrate
from scipy import special

x1,w = polynomial.laguerre.laggauss(100)

t = 10
f = lambda x: x**(t-1)

I = np.sum(f(x1)*w) 
print(I)
