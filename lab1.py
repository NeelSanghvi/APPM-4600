# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:22:37 2024

@author: 2021n
"""
import numpy as np

def main():
    a = np.array([[1,2],[3,4]])
    b = np.array([1,2])
    
    x = b@a
    print(x)
if __name__ == "__main__":
    main()