where = [[False] * 100 for _ in range(100)]

N = int(input())

for _ in range(N):
    row,col = map(int,input().split())
    
    for i in range(row, row+10):
        for j in range(col,col+10):
            where[i][j] = True

space = 0
for i in where:
    space += i.count(True)

print(space)
