import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect

def f(x):
    return x**3 - 3.23*x**2 - 5.54*x + 9.84

x = np.linspace(-4, 5)
plt.plot(x, f(x))
plt.axhline(0, color='red')
plt.axvline(0, color='red')
plt.show()