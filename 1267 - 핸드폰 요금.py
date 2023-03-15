N = int(input())

time = list(map(int, input().split()))
Y = 0
M = 0

for i in time:
    Y += ((i // 30) + 1) * 10
    M += ((i // 60) + 1) * 15

if Y > M:
    print(f"M {M}")
elif Y < M:
    print(f"Y {Y}")
else:
    print(f"Y M {M}")