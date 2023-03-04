day = int(input())

cars = list(map(int, input().split()))

cal = day - (day // 10) * 10

count = 0
for i in cars:
    if i == cal: count += 1

print(count)
