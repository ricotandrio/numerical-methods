import numpy as np

# function
f = lambda x: 4 * x ** 3 - 3 * x ** 2 + 3

a = 3
b = 5
n = 77 # number of points, (n - 1) is number of panels

height = (b - a) / (n - 1)
x = np.linspace(a, b, n)

y = f(x)

trapezoid = height / 2 * (y[0] + np.sum(2 * y[1:n-1]) + y[n-1])

print(trapezoid)
