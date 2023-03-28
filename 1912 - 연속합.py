import sys
n = int(input())

n_list = [0] + list(map(int, sys.stdin.readline().split()))

n_col = [0]

for i in range(len(n_list)-1):
    n_col.append(max(n_col[i] + n_list[i+1], n_list[i+1]))

print(max(n_col[1:]))
    