import numpy as np

f = lambda x: 4 * x ** 3 - 3 * x ** 2 + 3

a = 3
b = 5
n = 77

height = (b - a) / (n - 1)
x = np.linspace(a, b, n)

y = f(x)
left = height * np.sum(y[:n - 1]) # left riemann
right = height * np.sum(y[1:]) # right riemann

x_mid = (x[:n - 1] + x[1:]) / 2
y_mid = f(x_mid)
mid = height * np.sum(y_mid) # mid riemann

trapezoid = height / 2 * (y[0] + np.sum(2 * y[1:n-1]) + y[n-1]) # trapezoid

print(left, right, mid, trapezoid)
