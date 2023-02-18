M, N = map(int, input().split())
res = [False] * 2 + [True] * (N-1)
num = []

for i in range(2,N+1):
    if res[i]:
       num.append(i)
       for j in range(2*i, N+1, i):
            res[j] = False

for i in range(len(num)):
    if num[i] >= M:
        print(num[i])