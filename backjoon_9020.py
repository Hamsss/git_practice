T = int(input())
num = []


for i in range(T):
    num.append(int(input()))
    

check = [False] * 2 + [True] * (9999)

for i in range(2, 10001):
    if check[i]:
        for j in range(i, 10001, i):
            check[j] = False