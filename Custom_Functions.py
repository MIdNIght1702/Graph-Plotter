import matplotlib.pyplot as plt
import scipy.integrate as integrate
import math
import numpy as np


k  = 2

label1 = r'$\gamma = 5\%, \delta = 1\%, k_0 = $'+str(k)
label2 = r'$\gamma = 10\%, \delta = 2\%, k_0 = $'+str(k)



x_data = np.arange(-20,20,0.1)
y_data1 = np.arange(-20,20,0.1)
y_data2 = np.arange(-20,20,0.1)



def f(x):
    return integrate.quad(lambda k: math.sin(k*x**2),k_low,k_high)


k_low = k*0.05
k_high = k*0.01
i = 0

for items in x_data:
    y_data1[i] = f(x_data[i])[0]
    i = i+1

k_low = k*0.05
k_high = k*0.01
i = 0



for items in x_data:
    y_data2[i] = f(x_data[i])[0]
    i = i+1

fig = plt.figure(1,figsize = (4,4))
plt.plot(x_data,y_data1, color ="blue", linestyle = '--', label =label1)
plt.plot(x_data,y_data1, color ="blue", linestyle = '--', label =label2)

plt.ylim(-0.2,0.05)
plt.legend()

plt.xlabel(r'x (n) ')
plt.ylabel(r'$\int_{-k_0*\gamma}^{k_0*\delta} sin(k*x^2) dk$')

fig.savefig('example.png', dp1 = 300)