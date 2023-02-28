first = 1
second = 1

sum = 0
line = 1
count = 0
what = int(input())

while(1):
    sum += line
    if (sum >= what):
        count = what - (sum - line)
        break
    line += 1

if line%2==0:
    second = line
    for i in range(count-1):
        second -= 1
        first += 1
else:
    first = line
    for i in range(count-1):
        first -= 1
        second += 1

print(f"{first}/{second}")

