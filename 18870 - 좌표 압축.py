import sys

N = int(input())

X_n = list(map(int, sys.stdin.readline().split()))

Sorted_Xn = sorted(list(set(X_n)))

dict_X = {Sorted_Xn[i] : i for i in range(len(Sorted_Xn))}

for i in range(N):
    print(dict_X[X_n[i]], end = " ")



