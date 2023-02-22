N,M = map(int,input().split())

numbers = [i for i in range(1,N+1)]

for _ in range(M):
    i,j = map(int,input().split())
    val = []
    for a in range(i,j+1):
        val.append(numbers[a-1])
    
    val = val[::-1]
    count = 0
    
    for a in range(i,j+1):
        numbers[a-1] = val[count]
        count += 1

print(*numbers)
    
    
            

