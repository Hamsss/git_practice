import sys

N, M = map(int,input().split())
listen = set()
look = set()

for _ in range(N):
    listen.add(sys.stdin.readline().rstrip())
    
for _ in range(M):
    look.add(sys.stdin.readline().rstrip())

c = sorted(list(listen & look))

print(len(c))
for i in range(len(c)):
    print(c[i])