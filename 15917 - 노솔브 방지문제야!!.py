import sys

for _ in range(int(input())):
    flag = 0
    i = 0
    a = int(sys.stdin.readline())
    while a >= 2**i:
        if a == 2**i:
            flag = 1 
            break
        else:
            i += 1
    print(flag)
            
    