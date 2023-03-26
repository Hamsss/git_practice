sosu = [False] + [True] * 1041
for i in range(2,len(sosu)):
    if sosu[i]:
        for j in range(i*i, len(sosu), i):
            sosu[j] = False

N = input()
small,big = {}, {}
for i in range(26):
    small[chr(97+i)] = 1+i
    big[chr(65+i)] = 27+i

s_key, b_key = small.keys(), big.keys()
result = 0

for j in range(len(N)):
    if N[j] in s_key: result += small[N[j]]
    else: result += big[N[j]]

if sosu[result]: print("It is a prime word.")
else: print("It is not a prime word.")







