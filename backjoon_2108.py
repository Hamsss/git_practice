import sys
N = int(input())
num = []
count = [0] * 8001

for i in range(N):
    num.append(int(sys.stdin.readline()))
    
num.sort()

for i in num: 
    count[i] += 1

result = 0
temp = 0    
    
for i in range(-4000, 4001):
    if count[i] == max(count):
        result = i
        temp += 1
        if temp == 2:
            break

print(int(sum(num))/N))
print(num[N//2])
print(result)
print(max(num) - min(num))