num = []
result = 0

for i in range(7):
    number = int(input())
    if number % 2 == 1:
        num.append(number)

for odds in num:
    result += odds

if result > 0:
    print(result)
    print(min(num))
else:
    print(-1)
