import sys


N, X = map(int, sys.stdin.readline().split())
visitors = tuple(map(int, sys.stdin.readline().split()))


first_v = visitors[0]
cur_sum = sum(visitors[0:X])
max_sum = cur_sum
repeated = 1

for n in range(1, N - X + 1):
    cur_sum = cur_sum - visitors[n - 1] + visitors[n + X - 1]
    if cur_sum > max_sum:
        max_sum = cur_sum
        repeated = 1
    elif cur_sum == max_sum:
        repeated += 1

if max_sum > 0:
    print(max_sum)
    print(repeated)
else:
    print('SAD')
