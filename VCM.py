import numpy as np
import math

T = [140,160,180,200,220,240,260,280,300,320,340,360,380,400,420]
P = [2.03e-5,5.04e-4,5.41e-3,3.3e-2,0.135,0.416,1.04,2.20,4.15,7.12,11.4,17.2,24.9,34.8,47.5]

f = lambda x: x**(-1)
g = lambda x: math.log(x)

s = lambda x: x**2
c = lambda x: x**3
q = lambda x: x**4

X = np.array(list(map(f,T)))
Xs = np.array(list(map(s,X)))
Xc = np.array(list(map(c,X)))
Xq = np.array(list(map(q,X)))
Y = np.array(list(map(g,P)))

Sx_0 = len(X)
Sx_1 = sum(X)
Sx_2 = sum(Xs)
Sx_3 = sum(Xc)
Sx_4 = sum(Xq)
Sy = sum(Y)
Syx_1 = Y @ X
Syx_2 = Y @ Xs

M = np.array([[Sx_4,Sx_3,Sx_2],[Sx_3,Sx_2,Sx_1],[Sx_2,Sx_1,Sx_0]])
Minv = np.linalg.inv(M)
d = np.array([[Syx_2],[Syx_1],[Sy]])

z = Minv @ d
A = z[0][0]
B = z[1][0]
C = z[2][0]

def Psat1(T):
    x = T**(-1)
    y = (-144381)*(x**2) + (-1071.69*x) + (8.70353)
    p = math.exp(y)
    return p
