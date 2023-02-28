N = int(input())
num = []

for _ in range(N):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)
    
# for i in range(len(num)):
#     for j in range(i,len(num)):
#         if num[i] > num[j]:
#             temp = num[i]
#             num[i] = num[j]
#             num[j] = temp