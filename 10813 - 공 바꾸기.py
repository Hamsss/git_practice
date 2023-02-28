N, M = map(int,input().split())

bowl = [i for i in range(1,N+1)]

for i in range(M):
    i, j = map(int,input().split())
    temp = bowl[i-1]
    bowl[i-1] = bowl[j-1]
    bowl[j-1] = temp

print(*bowl)

