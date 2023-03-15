import sys

N = int(input())
size = list(map(int, sys.stdin.readline().split()))
cluster = int(input())
need = 0

for s in size:
    if s % cluster:
        need += (s // cluster + 1) * cluster
    else:
        need += s // cluster * cluster
        
print(need)