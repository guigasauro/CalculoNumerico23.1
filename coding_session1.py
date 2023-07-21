import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect

def f(x):
    return x**3 - x**2 - 6.54*x + 11.98

x = np.linspace(-4, 5)
plt.plot(x, f(x))
plt.axhline(0, color='red')
plt.axvline(0, color='red')
plt.show()