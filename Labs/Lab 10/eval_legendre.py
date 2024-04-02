# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 07:53:13 2024

@author: 2021n
"""

def eval_legendre(n,x):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, x]
    else:
        p = [1, x]
        for i in range(2, n + 1):
            p.append(((2*i - 1)*x * p[i-1] - (i - 1) * p[i-2]) / i)
        return p
    
n = 3
x = 0.5
result = eval_legendre(n, x)
