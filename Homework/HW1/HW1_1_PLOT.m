clc; close all; clear

x = 1.920:0.001:2.090;

p = x.^9-18*x.^8+ 144*x.^7 - 672*x.^6+ 2016*x.^5-4032*x.^4+ 5376*x.^3-4608*x.^2+2304*x-512;
f = (x-2).^9;
g = p-f;

figure(1);
hold on
plot(x,p,'DisplayName',strcat('y = p(x)'));
plot(x,f,'DisplayName','y = f(x)');
legend('show',Interpreter=("latex"));
title("Expanded vs Expression",Interpreter="latex");
xlabel('x',Interpreter="latex");
ylabel('y', Interpreter="latex");

hold off
