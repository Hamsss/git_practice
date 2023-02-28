# 소수 구하기
sosu = [False] * 2 + [True] * 9999

for i in range(2,10001):
    if sosu[i]:
       for j in range(2*i, 10001, i):
            sosu[j] = False

# 결과 저장을 위한 리스트
res = []

for _ in range(int(input())):
    n = int(input())
    a = n // 2
    b = a

    while 1:
        if sosu[a] and sosu[b]:
            res.append([a,b])
            break
        else:
            a -= 1
            b += 1
    
for i in range(len(res)):
    print(f"{res[i][0]} {res[i][1]}")