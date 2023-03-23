import sys
from math import gcd

n =int(input())
numbers = list(map(int, sys.stdin.readline().split()))

front_gcd = [0] * (n+1)
back_gcd = [0] * (n+1)

front_gcd[0] = numbers[0]
back_gcd[-2] = numbers[n-1]
for i in range(n-1):
    front_gcd[i+1] = gcd(front_gcd[i],numbers[i+1])
    back_gcd[-i-3] = gcd(back_gcd[-i-2], numbers[-2-i])

output = []

for i in range(n):
    res = gcd(front_gcd[i-1],back_gcd[i+1])
    if numbers[i] % res == 0:
        continue
    output.append((res,numbers[i]))

output.sort()
print(' '.join(map(str, output[-1])) if output else -1)