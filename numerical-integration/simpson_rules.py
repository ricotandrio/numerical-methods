import numpy as np

# function
f = lambda x: np.e ** (x)

a = 0
b = 4
n = 11 # number of points, (n - 1) is number of panels

h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
y = f(x)

def simpson_calculate(simspon1_3, simpson3_8):
    if((n - 1) % 2 == 0):
        # if the number of panels is even, calculate all panels using Simpson's 1/3 rule.
        simpson1_3 = (h/3) * (y[0] + 2 * sum(y[2:n - 2: 2]) + 4 * sum(y[1:n - 1: 2]) + y[n - 1])
    else:
        # if the number of panels is odd, calculate the first three panels using Simpson's 3/8 rule.
        simpson3_8 = (3 * h / 8) * (y[0] + 3 * y[1] + 3 * y[2] + y[3])
        simpson1_3 = (h/3) * (y[3] + 2 * sum(y[5:n - 2: 2]) + 4 * sum(y[4:n - 1: 2]) + y[n - 1])

    print("simpson 1/3 result is {}".format(simpson1_3))
    print("simpson 3/8 result is {}".format(simpson3_8))
    print("integral result by simpson's integration is {}".format(simpson1_3 + simpson3_8))

simpson_calculate(0, 0)

