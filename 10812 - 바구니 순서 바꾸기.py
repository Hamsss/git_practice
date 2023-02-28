N,M = map(int, input().split())

line = [i for i in range(1,N+1)]

for i in range(M):
    b, e, m = map(int,input().split())
    
    temp = []
    
    for i in range(m,e+1):
        temp.append(line[i-1])
    
    for i in range(b,m):
        temp.append(line[i-1])
    
    count = 0
    
    for i in range(b,e+1):
        line[i-1] = temp[count]
        count += 1

print(*line)
    