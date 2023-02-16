N = int(input())
num = list(map(int,input().split()))
answer = 0

for i in num:
    count = 0
    for j in range(2, max(num)+1):
        if i % j == 0:
            count += 1
    
    if count == 1:
        answer += 1

print(answer)
        



