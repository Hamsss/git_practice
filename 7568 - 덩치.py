import sys
human = []

for _ in range(int(input())):
    human.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(human)):
    rank = 1
    for j in range(len(human)):
        if human[i][0] < human[j][0] and human[i][1] < human[j][1]:
                rank += 1
    print(rank, end = " ")