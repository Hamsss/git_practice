# 11650 좌표정렬하기(1)_X축 우선순위
import sys
dot1 = []

for _ in range(int(input())):
    dot1.append(list(map(int,sys.stdin.readline().split())))

dot1.sort()

for i in range(len(dot1)):
    sys.stdout.writelines(f"{dot1[i][0]} {dot1[i][1]}\n")


# 11651 좌표정렬하기(2)_Y축 우선순위
import sys
dot2 = []

for _ in range(int(input())):
    a = list(map(int,sys.stdin.readline().split()))
    a.reverse()
    dot2.append(a)

dot2.sort()

for i in range(len(dot2)):
    sys.stdout.writelines(f"{dot2[i][1]} {dot2[i][0]}\n")
    
    

