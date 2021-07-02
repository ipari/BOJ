import sys
 
 
a = int(sys.stdin.readline())
x = int(sys.stdin.readline())
d = 10 ** 9 + 7
 
# 0b1101 -> [1, 0, 1, 1]
binary = bin(x)
binary = [int(i) for i in str(binary)[2:][::-1]]
 
# 지수 별 나머지 계산
remainders = {}
# n = 1
r = a % d
remainders[1] = r
# n >= 2
for n in range(1, len(binary)):
    remainders[n + 1] = remainders[n] ** 2 % d
 
# 결과값 계산
v = 1
for i, n in enumerate(binary):
    if n == 0:
        continue
    v = ((v % d) * remainders[i + 1] % d)
 
print(v)
