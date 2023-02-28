case = []

while 1:
    n = int(input())
    if n == 0:
        break
    case.append(n)

# val = max(case) -> 시간이 아주 조금 더 걸림    
# 소수구하기    
res = [False] * 2 + [True] * (2 * 123456 - 1)
for i in range(2, 2*123456+1):
    if res[i]:
        for j in range(i*2, 2*123456+1, i):
            res[j] = False

# 갯수 각각 구하기
for i in case:
    count = 0
    for j in range(i+1, i*2 + 1):
        if res[j]:
            count += 1
    print(count)
