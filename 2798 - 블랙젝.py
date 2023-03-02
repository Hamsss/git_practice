import sys

N,M = map(int,input().split())
list_a = list(map(int, sys.stdin.readline().split()))

list_a.sort()
min = 300000

for i in range(1, N-1):
    for j in range(i+1, N):
        for k in range(j+1, N+1):
            number = list_a[-i] + list_a[-j] + list_a[-k]
            if min > M - number and number < M:
                min = M - number
                res = number
            elif number == M:
                res = M
                break

print(res)
