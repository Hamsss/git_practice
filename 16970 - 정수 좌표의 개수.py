N, M, K = map(int,input().split())

state = [[False] * (N+1)]*(M+1)

for i in range(K):
    for j in range(N):
        for k in range(M):
            state 