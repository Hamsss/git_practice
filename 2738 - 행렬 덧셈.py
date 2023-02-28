N, M = map(int,input().split())
A_list = []

for _ in range(N*2):
    A_list.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        print(A_list[i][j] + A_list[i+N][j], end = " ")
    print()
