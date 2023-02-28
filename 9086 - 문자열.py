T = int(input())
a = []

for _ in range(T):
    a.append(input())

for i in range(T):
    print(f"{a[i][0]}{a[i][-1]}")