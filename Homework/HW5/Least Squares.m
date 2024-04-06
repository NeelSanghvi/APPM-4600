clear;
clc;

M = [1,0;1,1;1,2;1,3];
W = diag(4);
W(1,1) = 1;
W(2,2) = 4;
W(3,3) = 9;
W(4,4) = 6;

Aw = M'*W*M;
A = M'*M;

y = [1;4;2;6];

bw = M'*W*y;
b = M'*y;

coeff_w = Aw\bw;

coeff = A\b;

x = [0;1;2;3];

figure(1);
hold on
legend on
plot(x,coeff(1) + coeff(2).*x,'DisplayName','Unweighted')
plot(x,coeff_w(1) + coeff_w(2).*x,'DisplayName','Weighted')
hold off
