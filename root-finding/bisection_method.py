import numpy as np

f = lambda x: 5 * x ** 3 + 7 * x ** 2 + 4 * x + 5

coordinates = [
  	[2, 4],
  	[-3, 4],
 	[-2, 2],
 	[-7, 8],
 	[9, -4]
]

def bisection(a, b, tolerance = 0.01):
    if np.sign(f(a)) == np.sign(f(b)):
        return None

    mid = (a + b) / 2

    if np.abs(f(mid)) < tolerance:
        return mid
    elif np.sign(f(a)) == np.sign(f(mid)):
        return bisection(mid, b)
    elif np.sign(f(b)) == np.sign(f(mid)):
        return bisection(mid, a)

for x, y in coordinates:
    temp = bisection(x, y)
    if temp == None:
        print("not found")
    else:
        print("found at {}".format(temp))
