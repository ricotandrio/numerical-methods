import numpy as np

xs = [
    [
      [4, 2, -1],
      [1, -5, 2],
      [2, -1, -4]
    ],
    [
      [3, 4, 5],
      [-3, 7, -4],
      [1, -4, -2]
    ],
    [
      [9, -2, 3, 2],
      [2, 8, -2, 3],
      [-3, 2, 11, -4],
      [-2, 3, 2, 10]
    ]
]

ys = [
    [41, -10, 1],
    [34, -32, 62],
    [55, -14, 12, -21]
]


def gauss_seidel(x, y, tolerance = 0.01, iterate = 20):
    x = np.array(x)
    y = np.array(y)

    diagonal = np.diag(np.array(x))
    diagonal_abs = np.diag(np.abs(x))
    np.fill_diagonal(x, 0)
    off_diag = np.sum(np.abs(x), axis=1)

    if not np.all(diagonal_abs > off_diag):
        print("not diagonally dominant")
        return

    x = -x
    matrix_old = np.zeros(x[0].shape)
    for i in range(iterate):
        matrix_new = np.array(matrix_old)
        for k, row in enumerate(x):
            matrix_new[k] = (y[k] + np.dot(row, matrix_new)) / diagonal[k]

        print("step {}: {}".format(i + 1, matrix_new))
        dx = np.sqrt(np.dot(matrix_new - matrix_old, matrix_new - matrix_old))
        matrix_old = np.array(matrix_new)
        if dx < tolerance:
            print("convergent")
            return

    print("not convergent")
    return


for a, b in zip(xs, ys):
    print("STEP BREAK POINT")
    print("x : {}, y : {}".format(a, b))
    gauss_seidel(a, b)

