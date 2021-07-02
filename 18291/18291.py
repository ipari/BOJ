import sys
 
t_num = int(sys.stdin.readline())
tests = [int(sys.stdin.readline().strip()) for i in range(t_num)]
d = 10 ** 9 + 7
 
 
def to_binary(n):
    binary = str(bin(n))[2:]
    return [int(i) for i in binary[::-1]]
 
 
# 테스트값 중에서 최대 차수를 구한다.
max_n = max(tests)
 
# 최대 차수를 이진수로 변환했을 때의 자릿수를 구한다.
max_bin_n = len(to_binary(max_n))
 
# 지수 별 나머지 계산
remainders = {}
# n = 1
r = 2 % d
remainders[1] = r
# n >= 2
for n in range(1, max_bin_n):
    remainders[n + 1] = remainders[n] ** 2 % d
 
 
def get_result(test):
    # test <= 2 일 때 예외처리
    if test <= 2:
        return 1
    # 결과값 계산
    v = 1
    # 시작과 끝 징검다리 제외
    binary = to_binary(test - 2)
    for i, n in enumerate(binary):
        if n == 0:
            continue
        v = ((v % d) * remainders[i + 1] % d)
    return v
 
 
for test in tests:
    print(get_result(test))
