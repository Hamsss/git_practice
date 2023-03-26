import sys
N, K = map(int, input().split())
num = [0]+list(map(int,sys.stdin.readline().split()))
cul_sum = [0]

for i in range(1,N+1): 
    cul_sum.append(num[i] + cul_sum[i-1])

count = {}
result = 0
for i in range(0,N+1):
    result += count.get(cul_sum[i] - K, 0)
    count[cul_sum[i]] = count.get(cul_sum[i], 0) + 1

print(result)
# result = cul_sum[1:N+1].count(K)

# for i in range(1,N+1):
#     for j in range(i+1,N+1): 
#         cul_sum[j] -= num[i]
#     result += cul_sum[i+1:N+1].count(K)

# print(result)