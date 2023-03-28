import sys

H,W = map(int,input().split())

n_list = [0] + list(map(int,sys.stdin.readline().split()))
n_sum = sum(n_list)

prefix = [n_list[1]]
suffix = [n_list[-1]]

for i in range(2,W+1):
    if prefix[-1] < n_list[i]: prefix.append(n_list[i])
    else: prefix.append(prefix[-1])

for i in range(2,W+1):
    if suffix[-1] < n_list[-i]: suffix.append(n_list[-i])
    else: suffix.append(suffix[-1])

real_sum = 0

for i in range(0,W):
    real_sum += min(prefix[i],suffix[-1-i])
    
print(real_sum - n_sum)