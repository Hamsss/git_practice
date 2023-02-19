mat = []

for i in range(9):
    mat.append(list(map(int,input().split())))

row = 0
column = 0

for i in range(9):
    for j in range(9):
        if mat[row][column] <= mat[i][j]:
            row = i
            column = j

print(mat[row][column])
print(f"{row+1} {column+1}")