A,B,D = map(int, input().split())

sosu = [False] * 2 + [True] * (B+1)

for i in range(2, len(sosu)):
    if sosu[i]:
        for j in range(i*i, len(sosu), i):
            sosu[j] = False

count = 0
for i in range(A,B+1):
    if sosu[i] == True and str(D) in str(i):
        count += 1

print(count)