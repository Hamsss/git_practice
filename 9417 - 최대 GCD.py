import sys

def get_gcd(a,b):
    while a%b != 0:
        a, b = b, a%b
    return b

for _ in range(int(input())):
    number = list(map(int, sys.stdin.readline().split()))
    find_max = []
    
    for i in range(len(number)-1):
        for j in range(i+1, len(number)):
            find_max.append(get_gcd(number[i],number[j]))
    
    print(max(find_max))