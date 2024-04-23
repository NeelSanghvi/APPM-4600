# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:13:59 2024

@author: 2021n
"""

# get lgwts routine and numpy
import numpy as np;
import numpy.linalg as la;
import matplotlib.pyplot as plt

from scipy import integrate
from scipy import special


def eval_composite_trap(M,a,b,f):
  x = np.linspace(a,b,M);
  h = (b-a)/(M-1);
  w = h*np.ones(M);
  w[0]=0.5*w[0]; w[M-1]=0.5*w[M-1];

  I_hat = np.sum(f(x)*w);
  return I_hat,x,w;

def eval_composite_simpsons(M,a,b,f):
  x = np.linspace(a,b,M);
  h = (b-a)/(M-1);
  # Explain why this defines the weights for Simpsons
  w = (h/3)*np.ones(M);
  w[1:M:2]=4*w[1:M:2];
  w[2:M-1:2]=2*w[2:M-1:2];

  I_hat = np.sum(f(x)*w);
  return I_hat,x,w;


t = 10

f = lambda x: (x**(t-1))*np.exp(-x)
fpp = lambda x: (x**(t-3))*np.exp(-x)*(x**2 + (2 - 2*t)*x + t**2 - 3*t + 2)
#fpppp = lambda x: x**(t-5)*(x**4+(4-4*t)*x**3+(6*t**2-18*t+12)*x**2+(-4*t**3+24*t**2-44*t+24)*x+t**4-10*t**3+35*t**2-50*t+24)*np.exp(-x)


tol = 1e-4
a = 0
b = 100

Ms = np.arange(3,100000,200); nM = len(Ms)
I_trap = np.zeros((nM,))
I_simp = np.zeros((nM,))
# storage for error`
err_trap = np.zeros((nM,))
err_simp = np.zeros((nM,))
for iM in range(nM):
    M = Ms[iM]
    h = (b-a)/(M-1)
    I_trap[iM],_,_ = eval_composite_trap(M,a,b,f)
    #I_simp[iM],_,_ = eval_composite_simpsons(M, a, b, f)
    err_trap[iM] = ((b-a)/12)*(h**2)*np.abs(fpp(4.176))
    #err_simp[iM] = ((b-a)/180)*(h**4)*np.abs(fpppp(0))
        
print(err_trap[iM])

fig,ax = plt.subplots(1)
ax.semilogy(Ms,err_trap,'r--')
ax.set_xlabel('$M$')
ax.set_title('Trapezoid, t = ' + str(t))
ax.set_ylabel('Relative Error');
plt.show()

"""
fig,ax = plt.subplots(1)
ax.semilogy(Ms,err_simp,'b--')
ax.set_xlabel('$M$')
ax.set_title('Simpsons')
ax.set_ylabel('Relative Error');
plt.show()
"""

I_quad,abserr,infodict = integrate.quad(f,0,100,args=(), full_output=1, epsabs=tol)

print(I_quad)
print(infodict['neval'])