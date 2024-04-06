# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:04:41 2024

@author: 2021n
"""
import numpy as np
import matplotlib.pyplot as plt


def driver():
    N = 15;
    h = 2/(N)
    x = np.zeros(N+1)
    func = np.zeros(N+1)

    f = lambda x: 1/(1+(16*x)**2)
    
    x[0] = -1
    func[0] = f(x[0])

    for i in range(0,N+1):
        ##x[i] = np.cos(((2*i+1)*np.pi)/(2*(N+1)))
        x[i] = -1 + i*h
        func[i] = f(x[i])

    print(x)
     
    p = interpolation(f,x)
    
    plt.figure()
    plt.plot(x,func)
    plt.plot(x,p)
    plt.legend()
    plt.show()    
    


        

def interpolation(f,x):
    
    w = np.ones(len(x))

    for j in range(len(x)):
        for i in range(len(x)):
            if i != j:
                w[j] *= 1/(x[j]-x[i])
        
                
    num = np.zeros(len(x))
    denom = np.zeros(len(x))
    p = np.zeros(len(x))
    

    for j in range(0,len(x)):
        for i in range(0,len(x)):
            if i != j:
                num[j] += w[i]*f(x[i])/(x[j]-x[i])
                denom[j] += w[i]/(x[j]-x[i])
    
    for j in range(0,len(x)):
        p[j] = num[j]/denom[j]
        
    return p

if __name__ == '__main__':
  # run the drivers only if this is called from the command line
  driver()
