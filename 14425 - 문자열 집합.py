import sys

S = []
check = []
count = 0

N, M = map(int, input().split())

for _ in range(N):
    S.append(sys.stdin.readline().strip())

for _ in range(M):
    check.append(sys.stdin.readline().strip())

for word in check:
    if word in S:
        count += 1

print(count)