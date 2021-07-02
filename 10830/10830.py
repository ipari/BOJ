import sys
 
 
N, B = map(int, sys.stdin.readline().split())
ARR = []
for i in range(N):
    ARR.append(list(map(int, sys.stdin.readline().split())))
 
D = 1000
 
 
def matrix_mul(arr1, arr2):
    arr = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(sum((arr1[i][k] * arr2[k][j]) % D for k in range(N)) % D)
        arr.append(row)
    return arr
 
 
# B를 이진수로 변환하고 역순으로 뒤집은 배열을 만든다.
binary = bin(B)
binary = [int(i) for i in str(binary)[2:][::-1]]
 
 
# ARR ** (2 ** k) 들을 계산한다.
arrs = {}
arrs[1] = ARR
for n in range(1, len(binary)):
    arrs[n + 1] = matrix_mul(arrs[n], arrs[n])
 
 
# 위에서 구한 값들로 최종값을 계산한다.
I = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
arr = I
 
for i, x in enumerate(binary):
    if x == 0:
        continue
    arr = matrix_mul(arr, arrs[i + 1])
 
 
for row in arr:
    print(' '.join([str(v) for v in row]))
