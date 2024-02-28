# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:29:13 2024

@author: 2021n
"""

# import libraries
import numpy as np


# define routines
def bisection(f,fp,fpp,a,b,tol,Nmax):
    '''
    Inputs:
      f,fp,fpp,a,b       - function and it's derivatives and endpoints of initial interval
      tol, Nmax   - bisection stops when interval length < tol
                  - or if Nmax iterations have occured
    Returns:
      astar - approximation of root
      ier   - error message
            - ier = 1 => cannot tell if there is a root in the interval
            - ier = 0 == success
            - ier = 2 => ran out of iterations
            - ier = 3 => other error ==== You can explain
    '''

    '''     first verify there is a root we can find in the interval '''
    fa = f(a); fb = f(b);
    count = 0

    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier, count]

    ''' verify end point is not a root '''
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier, count]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier,count]

    while (count < Nmax):
      
      c = 0.5*(a+b)
      fc = f(c)
      print(c)
      
      fpc = fp(c)
      fppc = fpp(c)
      gpc = np.abs(fc*fppc/(fpc**2))
      
      if (gpc < 1):
        astar = c
        ier = 0
        return [astar, ier, count]

      if (fa*fc<0):
         b = c
      elif (fb*fc<0):
        a = c
        fa = fc
      else:
        astar = c
        ier = 3
        return [astar, ier, count]

      if (abs(b-a)<tol):
        astar = a
        ier =0
        return [astar, ier, count]
      
      count = count +1

    astar = a
    ier = 2
    return [astar,ier, count] 


# define routines
def newton(f,fp,p0,tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]
        



# use routines    
f = lambda x: np.exp(((x**2)+7*x-30)) - 1
fp = lambda x: (2*x+7)*np.exp(((x**2)+7*x-30))
fpp = lambda x: (4*(x**2)+28*x+51)*np.exp(((x**2)+7*x-30))
a = 2
b = 4.5

Nmax = 100
tol = 1e-3

[astar,ier, count] = bisection(f,fp,fpp,a,b,tol,Nmax)
p,pstar,info,it = newton(f,fp,astar,tol, Nmax)

print('the approximate root is',pstar)
print('the error message reads:',info)
print('The number of iterations are', it)




