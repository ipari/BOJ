import sys

n = int(sys.stdin.readline())


def get_fibonacci_num(n, cur_n=2, pprev=0, prev=1):
    if n == 0:
        return pprev
    if n == 1:
        return prev
    if n == cur_n:
        return pprev + prev
    return get_fibonacci_num(n, cur_n+1, pprev=prev, prev=pprev+prev)


print(get_fibonacci_num(n))
