import numpy as np

f = lambda x: -0.7654 * np.sqrt(max(x, 0))

# Runge-Kutta 4th order method
def runge_kutta_4th(t0, theta0, h, num_steps):
    t = [t0]
    theta = [theta0]
    for _ in range(num_steps):
        k0 = f(theta[-1]) * h
        k1 = f(theta[-1] + (k0/2)) * h
        k2 = f(theta[-1] + (k1/2)) * h
        k3 = f(theta[-1] + k2) * h
        t.append(t[-1] + h)
        theta.append(theta[-1] + ((1/6) * (k0 + (2 * k1) + (2 * k2) + k3)))
    return t, theta

# Initial conditions
t0 = 0
theta0 = 3.5
h = 0.75  # Step size
num_steps = 6  # Number of steps

# Solve the differential equation using Runge-Kutta 4th order method
t, theta = runge_kutta_4th(t0, theta0, h, num_steps)

# Print the results
for i in range(len(t)):
    print(f"Time: {t[i]}, Height: {theta[i]}")
