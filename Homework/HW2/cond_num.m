clear;

A = 0.5*[1,1;(1+10^-10),(1-10^-10)]

cond(A)

t = 0:pi/30:pi;
y = cos(t);
s = sum(t.*y)

Y = expm1(9.999999995000000*10^-10)
Y2 = exp(9.999999995000000-10^-10)-1

x =9.999999995000000*10^-10;
T = x + x^2/2 
R = exp(x)*x^3/6
T - Y
