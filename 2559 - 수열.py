import sys
N,K = map(int,input().split())
n_list = list(map(int, sys.stdin.readline().split()))
c_list = [0]
answer = []

for i in range(N): c_list.append(c_list[-1] + n_list[i])

for i in range(N - K + 1): answer.append(c_list[i+K] - c_list[i] )

print(max(answer))