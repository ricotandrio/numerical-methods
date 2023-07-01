import numpy as np

# Runge-Kutta 2nd order method
def runge_kutta_2nd(t0, theta0, h, num_steps):
    t = [t0]
    theta = [theta0]
    for _ in range(num_steps):
        k0 = h * -2.2067 * 10**-12 * (theta[-1]**4 - (81 * 10**8))
        k1 = h * -2.2067 * 10**-12 * ((theta[-1] + (k0/2))**4 - (81 * 10**8))
        t.append(t[-1] + h)
        theta.append(theta[-1] + k1)
    return t, theta

# Initial conditions
t0 = 0
theta0 = 1200
h = 240  # Step size
num_steps = 2  # Number of steps

# Solve the differential equation using Runge-Kutta 2nd order method
t, theta = runge_kutta_2nd(t0, theta0, h, num_steps)

# Print the results
for i in range(len(t)):
    print(f"Time: {t[i]}, Temperature: {theta[i]}")
