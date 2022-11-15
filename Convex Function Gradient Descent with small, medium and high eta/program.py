import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
import math


def f(x):
    return x ** 2

def deriv(x):
    return derivative(f,x)

y = np.linspace(-10.0, 10.0)

"""small eta"""
new_x = 7
previous_x = 0
step_multiplier = 0.1

x_list = [new_x]


for n in range(1000):
    previous_x = new_x
    gradient = deriv(previous_x)
    new_x = previous_x - step_multiplier * gradient
    
    x_list.append(new_x)

plt.subplot(212)
plt.title("Small eta:")
plt.plot(y, f(y), color='purple', label='Function')

values = np.array(x_list)
plt.scatter(x_list,f(values), color = 'red')


"""medium eta"""


new_x = 7
previous_x = 0
step_multiplier = 0.6

x_list = [new_x]


for n in range(1000):
    previous_x = new_x
    gradient = deriv(previous_x)
    new_x = previous_x - step_multiplier * gradient
    
    x_list.append(new_x)

plt.subplot(221)
plt.title("Medium eta:")
plt.plot(y, f(y), color='purple', label='Function')

values = np.array(x_list)
plt.scatter(x_list,f(values), color = 'red')

new_x = 7
previous_x = 0
step_multiplier = 1

x_list = [new_x]


for n in range(1000):
    previous_x = new_x
    gradient = deriv(previous_x)
    new_x = previous_x - step_multiplier * gradient
    
    x_list.append(new_x)

plt.subplot(222)
plt.title("Big eta:")
plt.plot(y, f(y), color='purple', label='Function')

values = np.array(x_list)
plt.scatter(x_list,f(values), color = 'red')

plt.grid(True)
plt.show()

