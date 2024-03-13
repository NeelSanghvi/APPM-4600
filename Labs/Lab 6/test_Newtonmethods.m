function test_Newtonmethods


F = @(x,y,z) [3*x-cos(y.*z)-1/2; x-81*(y+0.1).^2+sin(z)+1.06;...
              exp(-x.*y)+20*z+(10*pi-3)/3];
J = @(x,y,z) [3 z.*sin(y.*z) y.*sin(y.*z);...
             2*x -162*(y+0.1) cos(z);...
             -y.*exp(-x.*y) -x.*exp(-x.*y) 20];

         
         
% x0 = [0.1; -0.1; -0.1];

x0 = [7; 7; 7];

tol = 1e-9;
Nmax = 1000;


tic
for j = 1:20
[alpha, iter, ier] = Newton(F,J,x0, tol, Nmax);
end
tim = toc/20;

fprintf('Newton: approximation=  [');
fprintf('%g, ', alpha(1:end-1));
fprintf('%g]\n', alpha(end));

fprintf('Newton: number of iterations =%i\n',iter);
fprintf('Newton: time =%2.6f\n',tim);
fprintf('Newton: error message =%i\n',ier);


tic
for j = 1:20
[alpha, iter, ier] = Newton_lazy(F,J,x0, tol, Nmax);
end
tim = toc/20;

fprintf('Lazy Newton: approximation = [');
fprintf('%g, ', alpha(1:end-1));
fprintf('%g]\n', alpha(end));
fprintf('Lazy Newton: number of iterations =%i\n',iter);
fprintf('Lazy Newton: time =%2.6f\n',tim);
fprintf('Lazy Newton: error message =%i\n',ier);


tic
for j = 1:20
[alpha, iter, ier] = Broyden(F,J,x0, tol, Nmax);
end
tim = toc/20;

fprintf('Broyden: approximation =[');
fprintf('%g, ', alpha(1:end-1));
fprintf('%g]\n', alpha(end));
fprintf('Broyden: number of iterations =%i\n',iter);
fprintf('Broyden: time =%2.6f\n',tim);
fprintf('Broyden: error message =%i\n',ier);

keyboard

return


function [alpha, iter, ier] = Newton(F,J,x0, tol, Nmax)

% tol = desired accuracy
% Nmax = max number of iterations



for j = 1:Nmax
   
    Ginv = inv(J(x0(1),x0(2),x0(3)));
    
    xk = x0 - Ginv*F(x0(1),x0(2),x0(3));
    
    if (norm(xk-x0) <tol)
        alpha = xk;
        ier = 0;
        iter = j;
        return
    end
    
    x0 = xk;
    
end

alpha = xk;
ier = 1;
iter = j;

return




function [alpha, iter, ier] = Newton_lazy(F,J,x0, tol, Nmax)

% tol = desired accuracy
% Nmax = max number of iterations

G0inv = inv(J(x0(1),x0(2),x0(3)));

for j = 1:Nmax
    xk = x0 - G0inv*F(x0(1),x0(2),x0(3));
    if (norm(xk-x0) <tol)
        alpha = xk;
        ier = 0;
        iter = j;
        return
    end
    x0 = xk;
end

alpha = xk;
ier = 1;
iter = j;

return


function [alpha, iter, ier] = Broyden(F,J,x0, tol, Nmax)

% tol = desired accuracy
% Nmax = max number of iterations

%  Sherman-Morrison 
% (A+xy^T)^{-1} = A^{-1}-1/p*(A^{-1}xy^TA^{-1})
% where p = 1+y^TA^{-1}Ax



%  newton
%  x_k+1 = xk -(G(x_k))^{-1}*F(x_k)


% for broyeden 
%  x = [F(xk)-F(xk-1)-\hat{G}_k-1(xk-xk-1)
%  y = x_k-x_k-1/||x_k-x_k-1||^2

% implemented as in equation (10.16) on page 650 of text

% initialize with 1 newton step
A0 = J(x0(1),x0(2),x0(3));

v = F(x0(1),x0(2),x0(3));

A = inv(A0);

s = -A*v;
xk = x0+s; % x1

for j = 2:Nmax
    w = v;                     %(save v from previous step);
    v = F(xk(1),xk(2),xk(3));  % create new v
    y = v-w;                   % y_k = F(xk)-F(xk-1)
    z = -A*y;                  % -A_{k-1}^{-1}y_k
    p = -s'*z;                 % p = s_k^tA_{k-1}^{-1}y_k
    u = s'*A; 
    A = A+1/p*(s+z)*u;         % A = A_k^{-1} via Morrison formula
    s = -A*v;                  % s = -A_k^{-1}F(x_k)
    xk = xk+s;
    if norm(s)<tol
        alpha = xk;
        ier = 0;
        iter = j;
        return
    end
end     

alpha = xk;
ier = 1;
iter = j;

return
