import numpy as np

f = lambda x: 5 * x ** 3 + 7 * x ** 2 + 4 * x + 5
g = lambda x: 15 * x ** 2 + 14 * x + 4

def newton_raphson(x0, tolerance, iterate_var, max_iterate):
    x1 = x0 - f(x0) / g(x0)

    if np.abs(f(x1)) < tolerance:
        print("root found at {}".format(x1))
        return
    print("step {}, root = {}".format(iterate_var, x1))
    if iterate_var >= max_iterate:
        print("[STOP]")
        return
    newton_raphson(x1, tolerance, iterate_var + 1, max_iterate)

newton_raphson(30, 0.01, 1, 15)



