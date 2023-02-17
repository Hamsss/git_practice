M = int(input())
N = int(input())
answer = 0

if M == 1:
    for i in range(2,N+1):
        count = 0
        for j in range(1,i):
            if j == 1:
                continue
            else:
                if i % j == 0:
                    count += 1
else:
    for i in range(M, N+1):        

    