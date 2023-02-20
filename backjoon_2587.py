num = [int(input()) for _ in range(5)]
sum = 0
num.sort()

for i in num:
    sum += i
    
print(sum//5)
print(num[2])
