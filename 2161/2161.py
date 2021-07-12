import sys


N = int(sys.stdin.readline())

deck = [x for x in range(1, N + 1)]
result = []

while deck:
    result.append(str(deck[0]))
    deck = deck[2:] + deck[1:2]

print(' '.join(result))
