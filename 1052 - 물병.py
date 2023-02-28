N, K = map(int, input().split())
count_bottle = 0

while bin(N).count('1') > K:
    N += 1
    count_bottle += 1
    
print(count_bottle)


# import sys
# N, K = map(int, sys.stdin.readline().split())
# cnt = 0
# while bin(N).count('1') > K :
#     idx = bin(N)[::-1].index('1')
#     cnt += 2**idx
#     N += 2**idx
# print(cnt)

# N, K = map(int, input().split())
# count = 0
# num = 0
# count_bottle = 0

# while N > K:
#     if N % 2 == 1:
#         N += 1
#         count += 2 ** num
#         count_bottle += 1
#         if K + 1 < count_bottle:
#             break
#     N = N // 2
#     num += 1
    
# print(count)