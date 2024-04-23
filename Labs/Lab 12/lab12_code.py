import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time 


def driver():

     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     N = 5000
 
     ''' Right hand side'''
     b = np.random.rand(N,1)
     A = np.random.rand(N,N)
     
     t1_sol = time.perf_counter_ns()
     x = scila.solve(A,b)
     t2_sol = time.perf_counter_ns()
     
     t_sol = t2_sol - t1_sol
     
     print(t_sol/1e9)
     
     t3_lu_fac = time.perf_counter_ns()
     lu, piv = scila.lu_factor(A)
     t4_lu_fac = time.perf_counter_ns()
     
     t_lu_fac = t4_lu_fac - t3_lu_fac
     
     print(t_lu_fac/1e9)
     
     t5 = time.perf_counter_ns()
     x2 = scila.lu_solve((lu, piv), b)
     t6 = time.perf_counter_ns()
     
     t_lu_sol = t6 - t5
     
     print(t_lu_sol/1e9)
     
     print((t_sol - (t_lu_fac+t_lu_sol))/1e9)
     
     test = np.matmul(A,x)
     r = la.norm(test-b)
     
     print(r)

     ''' Create an ill-conditioned rectangular matrix '''
     N = 10
     M = 5
     A = create_rect(N,M)     
     b = np.random.rand(N,1)
     

     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B     
          
  
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()       
