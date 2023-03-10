N = int(input())
count = 0

for a in range(1, 500):
    for b in range(a+1,500):
        if a**2 + N == b ** 2:
            count += 1
print(count)