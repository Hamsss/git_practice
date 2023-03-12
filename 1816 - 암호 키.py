sosu = [False] * 2 + [True] * 999999
num = []

for i in range(2, len(sosu)):
    if sosu[i]:
        num.append(i)
        for j in range(2*i, len(sosu), i):
            sosu[j] = False

for _ in range(int(input())):
    flag = 0
    check = int(input())
    for i in num:
        if check % i == 0:
            flag = 1
            print("NO")
            break
    if flag == 0:
        print("YES")