import sys


X, Y = map(str, sys.stdin.readline().split())


def rev(n):
    return int(str(n)[::-1])


print(rev(rev(X) + rev(Y)))
