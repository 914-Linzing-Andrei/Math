import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
import math

""" x4+x3−2x2−2x"""
def f2(x):
    return x ** 4 + x ** 3 - 2 * (x ** 2) - 2 * x

def deriv2(x):
    return derivative(f2,x)

y = np.linspace(-10.0, 10.0)
plt.xlim(-2,3)
plt.ylim(-3,6)
new_x = -2
previous_x = 0
step_multiplier = 0.002
precision = 0.00001

x_list = [new_x]


for n in range(100):
    previous_x = new_x
    gradient = deriv2(previous_x)
    new_x = previous_x - step_multiplier * gradient
    
    x_list.append(new_x)

plt.title("Non convex function:")
plt.plot(y, f2(y), color='purple', label='Function')

values = np.array(x_list)
plt.scatter(x_list,f2(values), color = 'red')
plt.grid(True)
plt.show()
