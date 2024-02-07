# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, np.pi, 30)

# Create the vector y = cos(t)
y = np.cos(t)

# Calculate the sum of t*y from index 1 to the end of the vector
s = np.dot(t, y);


print("The sum is:", s)

R = 1.2
delta = 0.1
f = 15
p = 0

theta = np.linspace(0, 2*np.pi, 1000)
x = R*(1 + delta*np.sin(f*theta + p))*np.cos(theta)
y = R*(1 + delta*np.sin(f*theta + p))*np.sin(theta)


plt.figure(1)

plt.plot(x, y)
plt.title('Problem 4b.1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

num = np.linspace(1, 10,10)
for i in num:
    R = i
    delta = 0.05
    f = 2+i
    p = np.random.uniform(0,2)

    theta = np.linspace(0, 2*np.pi, 1000)
    x = R*(1 + delta*np.sin(f*theta + p))*np.cos(theta)
    y = R*(1 + delta*np.sin(f*theta + p))*np.sin(theta)

    plt.figure(2)
    plt.plot(x, y)
    plt.title('Problem 4b.2')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

