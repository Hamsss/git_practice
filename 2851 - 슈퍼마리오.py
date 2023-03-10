import sys
mushroom = []
result = 0
min_num = 101

for _ in range(10):
    mushroom.append(int(sys.stdin.readline().strip()))

for i in range(10):
    result += mushroom[i]
    if abs(100 - result) > min_num:
        result -= mushroom[i]
        break
    elif abs(100 - result) == min_num:
        break
    min_num = abs(100 - result)
    
print(result)