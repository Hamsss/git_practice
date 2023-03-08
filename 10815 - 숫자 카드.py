import sys

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

M = int(input())
answers = list(map(int, sys.stdin.readline().split()))

T_F = []

for num in answers:
    flag = 0
    start = 0
    end = N - 1
    mid = N // 2
    while num != numbers[mid]:
        if end == start:
            T_F.append(0)
            break
        if num < numbers[mid]:
            end = mid - 1
        elif num > numbers[mid]:
            start = mid
        mid = (end + start + 1) // 2
        
    else:
        T_F.append(1)
        
print(*T_F)
