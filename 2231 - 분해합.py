N = int(input())
num = 0
flag = 1
numbers = [0] * 7

while N != num:
    num = 0
    numbers[0] += 1
    for j in range(0,7):
        if numbers[j] == 10:
            numbers[j] = 0
            numbers[j+1] += 1

    for i in range(7):
        num += 10**i * numbers[i] + numbers[i]
    
    if num >= 999960:
        flag = 0
        break

numbers.reverse()
number = 0

for i in range(1, len(numbers)+1):
    number += numbers[-i] * 10**(i-1)

if flag == 0:
    print(0)
else:
    print(number)