A, B, V = map(int, input().split())

distance = A - B
high = V - A

if high % distance:
    day = int(high / distance) + 1
else:
    day = int(high / distance)

print(day + 1)