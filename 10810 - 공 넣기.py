N, M = map(int,input().split())

bowl = [0] * N

for _ in range(M):
    i,j,k = map(int,input().split())
    for a in range(i,j+1):
        bowl[a-1] = k

print(*bowl)