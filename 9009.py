import sys


n_count = int(sys.stdin.readline())
ns = []
for _ in range(n_count):
    ns.append(int(sys.stdin.readline()))

# 피보나치 수열 미리 계산
max_n = max(ns)
fibo = [0, 1]
while max_n > fibo[-1]:
    fibo.append(fibo[-2] + fibo[-1])


def get_result(n):
    # 피보나치 수의 조합 계산
    result = []
    for v in fibo[:1:-1]:
        if v <= n:
            result.append(v)
            n -= v
    return result


# 각 테스트에 대하여 결과 출력
for n in ns:
    result = get_result(n)[::-1]
    print(' '.join([str(x) for x in result]))
