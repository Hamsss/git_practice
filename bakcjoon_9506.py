answer = []

while 1:
    count = []
    n = int(input())
    
    if n == -1:
        break
    
    for i in range(1, n//2 + 1):
        if n % i == 0:
            count.append(i)
    
    if sum(count) == n:
        answer.append([n, *count])
    else:
        answer.append([n, "is Not perfect."])
    
for i in range(len(answer)):
    if answer[i][1] is int:
        print(answer[i][0], end=' =')
        print(str(answer[i][1:]).join(' + '))
    else:
        print(*answer)
        
            