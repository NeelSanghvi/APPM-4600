# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:22:37 2024

@author: 2021n
"""
import numpy as np

def main():
    a = np.array([[1,2],[3,4]]) #This creates a 2 by 2 matrix
    b = np.array([1,2]) #This creates a 2 by row vector
    
    x = b@a #This does the matrix multiplication of row vector (b) and matrix a
    print(x) #This prints the resultant matrix
    
if __name__ == "__main__":
    main()