import sys

N, M = map(int,input().split())

chess = []
result = []

for i in range(N):
    chess.append(list(sys.stdin.readline().strip()))

for i in range(0,N-7):
    for j in range(0,M-7):
        count1 = 0
        count2 = 0
        for k in range(i, i+8):
            for x in range(j, j+8):
                if (k + x) % 2 == 0:
                    if chess[k][x] != 'B':
                        count1 += 1
                    if chess[k][x] != 'W':
                        count2 += 1
                else:
                    if chess[k][x] != 'W':
                        count1 += 1
                    if chess[k][x] != 'B':
                        count2 += 1
 
        result.append(count1)
        result.append(count2)                    

print(min(result))