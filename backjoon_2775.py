tenement = []

# 아파트 구성하기
for i in range(14):
    tenement.append([1])
    if i == 0:
        for j in range(0,13):
            tenement[i].append(tenement[i][j] + j+2)
    else:
        for j in range(0,13):
            tenement[i].append(tenement[i][j] + tenement[i-1][j+1])

T = int(input())
count = []

for i in range(T):
    k = int(input())
    n = int(input())
    count.append(tenement[k-1][n-1])

for i in range(len(count)):
    print(count[i])
    
