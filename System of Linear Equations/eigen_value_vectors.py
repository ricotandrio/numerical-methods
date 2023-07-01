import numpy as np
from numpy.linalg import eig

x = [
    [
        [2, 2, 4],
        [1, 3, 5],
        [2, 3, 4]
    ]
]

for i in x:
    a = np.array(i)
    w, v = eig(a)
    print('Eigen Value:\n {}'.format(w))
    print('Eigen Vector:\n {}'.format(v))

