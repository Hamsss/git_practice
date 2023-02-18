M = int(input())
N = int(input())
answer = []

for i in range(M, N+1):
    count = 0
    if i == 0:
        continue
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        answer.append(i)

if not answer:
    print(-1)
else:
    print(sum(answer))
    print(answer[0])

    