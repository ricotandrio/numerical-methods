import numpy as np

# function
f = lambda x: 4 * x ** 3 - 3 * x ** 2 + 3

a = 3
b = 5
n = 77 # number of points, (n - 1) is number of panels

height = (b - a) / (n - 1)
x = np.linspace(a, b, n)

y = f(x)
left = height * np.sum(y[:n - 1]) # left riemann
right = height * np.sum(y[1:]) # right riemann

x_mid = (x[:n - 1] + x[1:]) / 2
y_mid = f(x_mid)
mid = height * np.sum(y_mid) # mid riemann

print(left, right, mid)
