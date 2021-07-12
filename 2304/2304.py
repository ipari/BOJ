import sys


n = int(sys.stdin.readline())

info = []
for i in range(n):
    info.append(list(map(int, sys.stdin.readline().split())))

info = sorted(info, key=lambda x: x[0])

# 정방향 탐색
left_pillars = []
for x, y in info:
    if not left_pillars or y > left_pillars[-1][1]:
        left_pillars.append([x, y])

# 역방향 탐색
right_pillars = []
for x, y in info[::-1]:
    if not right_pillars or y > right_pillars[-1][1]:
        right_pillars.append([x, y])
    if y == left_pillars[-1][1]:
        break


def sum_area(pillars):
    area = 0
    for i in range(len(pillars) - 1):
        width = pillars[i + 1][0] - pillars[i][0]
        height = pillars[i][1]
        area += width * height
    return area


left_area = sum_area(left_pillars)
right_area = sum_area(right_pillars)
center_area = (right_pillars[-1][0] - left_pillars[-1][0] + 1) * left_pillars[-1][1]

area = left_area - right_area + center_area
print(area)
