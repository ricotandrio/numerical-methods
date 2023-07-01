import numpy as np

# runge-kutta 2nd order with heun's method
def heun(t0, theta0, h, num_steps):
    t = [t0]
    theta = [theta0]
    for _ in range(num_steps):
        k0 = -2.2067 * 10**-12 * (theta[-1]**4 - (81 * 10**8))
        k1 = -2.2067 * 10**-12 * ((theta[-1] + (k0 * h))**4 - (81 * 10**8))
        t.append(t[-1] + h)
        theta.append(theta[-1] + (((0.5 * k1) + (0.5 * k0)) * h))
    return t, theta

# Initial conditions
t0 = 0
theta0 = 1200
h = 240  # Step size
num_steps = 2  # Number of steps

# Solve the differential equation using Runge-Kutta 2nd order method
t, theta = heun(t0, theta0, h, num_steps)

# Print the results
for i in range(len(t)):
    print(f"Time: {t[i]}, Temperature: {theta[i]}")
