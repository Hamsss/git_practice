need = [1,1,2,2,2,8]
answer =[]

K,Q,L,B,N,P = map(int,input().split())
count = [K,Q,L,B,N,P]

for i in range(6):
    answer.append(need[i] - count[i])

print(*answer)