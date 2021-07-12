import sys


N = int(sys.stdin.readline())
D = 10 ** 9 + 7


def matrix_mul(arr1, arr2):
    arr = []
    for i in range(2):
        row = []
        for j in range(2):
            row.append(sum((arr1[i][k] * arr2[k][j]) % D for k in range(2)) % D)
        arr.append(row)
    return arr


def matrix_square(arr):
    return matrix_mul(arr, arr)


binary = bin(N)[2:]
result = [[1, 0], [0, 1]]
cur = [[1, 1], [1, 0]]

for i, b in enumerate(binary[::-1]):
    if i > 0:
        cur = matrix_square(cur)
    if b == '1':
        result = matrix_mul(result, cur)

print((result[0][0] % D * result[0][1] % D) % D)
