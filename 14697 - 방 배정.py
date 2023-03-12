A,B,C,N = map(int, input().split())
flag = 0

for i in range(N//A+1):
    for j in range(N//B+1):
        for k in range(N//C+1):
            if A*i + B*j + C*k == N:
                flag = 1
                break
    if flag == 1: break

print(1) if flag == 1 else print(0)
                
