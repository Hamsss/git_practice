import sys
n,m = map(int,input().split())

n_list = [0] + list(map(int, sys.stdin.readline().split()))
cul_list = [0]

for i in range(n): cul_list.append(cul_list[i] + n_list[i+1])

for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    sys.stdout.write(f"{cul_list[e] - cul_list[s-1]}\n")
