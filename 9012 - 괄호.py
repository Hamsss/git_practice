import sys

for _ in range(int(input())):
    kuohao = sys.stdin.readline().strip()
    a, b = 0,0
    arr = []
    flag = True
    for i in range(len(kuohao)):
        if kuohao[i] == '(':
            a += 1
            arr.append('(')
        else:
            b += 1
            if len(arr) == 0:
                flag = False
            else:
                arr.pop()
    if a == b and flag == True: print("YES")
    else: print("NO")