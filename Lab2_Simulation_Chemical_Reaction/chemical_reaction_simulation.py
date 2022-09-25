import numpy as np

#initialize variable
a = np.zeros((100,),dtype=float)
b = np.zeros((100,),dtype=float)
c = np.zeros((100,),dtype=float)
t = np.zeros((100,))
a[0] = 100
b[0] = 50
t[0] = 0
delta_t = 0.1
k1 = 0.008
k2 = 0.002
N = 60

for i in range(1,N):
    a[i] = a[i-1]+(k2*c[i-1]-k1*a[i-1]*b[i-1])*delta_t;
    b[i] = b[i-1]+(k2*c[i-1]-k1*a[i-1]*b[i-1])*delta_t;
    c[i] = c[i-1]+(2*k1*a[i-1]*b[i-1]-2*k2*c[i-1])*delta_t;
    t[i] = t[i-1]+delta_t;

print("TIME","\tA(i)","\tB(i)","\tC(i)")
for i in range(N):
    print("%.2f"%t[i],"\t%.2f"%a[i],"\t%.2f"%b[i],"\t%.2f"%c[i])

