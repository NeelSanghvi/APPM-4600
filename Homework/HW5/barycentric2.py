# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:39:00 2024

@author: 2021n
"""

import numpy as np
import matplotlib.pyplot as plt


def driver():
    N = 15;
    h = 2/(N)
    x = np.zeros(N+1)
    func = np.zeros(N+1)

    f = lambda z: 1/(1+(16*z)**2)
    
    x[0] = -1
    func[0] = f(x[0])

    for i in range(0,N+1):
 ##       x[i] = np.cos(((2*i+1)*np.pi)/(2*(N+1)))
        x[i] = -1 + i*h
        func[i] = f(x[i])

    print(x)
     
    p = interpolation(f,x)
    
    plt.figure()
    plt.plot(x,f(x))
    plt.plot(x,p(x))
    plt.legend()
    plt.show()    
    


        

def interpolation(f,x):
    
    w = np.ones(len(x))

    for j in range(len(x)):
        for i in range(len(x)):
            if i != j:
                w[j] *= 1/(x[j]-x[i])
        
                
    num = lambda z: 0
    denom = lambda z: 0
    print(i)
    print(j)
    for i in range(0,len(x)):
        num = lambda z, curr_num=num: curr_num(z) + w[i]*f(x[i])/(z-x[i])
        denom = lambda z, curr_denom=denom: curr_denom(z) + w[i]/(z-x[i])
    
    print(1)
    p = lambda z: num(z)/denom(z)
    
    return p

if __name__ == '__main__':
  # run the drivers only if this is called from the command line
  driver()
