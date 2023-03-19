import sys

S = set()
count = 0

N, M = map(int, input().split())

for _ in range(N):
    S.add(sys.stdin.readline())

for _ in range(M):
    word = sys.stdin.readline()
    if word in S:
        count += 1

print(count)