import numpy as np
import matplotlib.pyplot as plt


step = 0.1

# define grid
x = np.arange(0, 2 * np.pi, step)

# define function
y = np.cos(x)

# vector of forward differences
forward_diff = np.diff(y) / step

# corresponding grid
x_diff = x[:-1:]

# exact solution
exact_solution = -np.sin(x_diff)

# plotting
plt.figure(figsize= (12, 8))
plt.plot(x_diff, forward_diff, '--', label = 'Finite difference approximation')
plt.plot(x_diff, exact_solution, label='Exact solution')
plt.legend()
plt.show()
