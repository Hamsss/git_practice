import sys

name = [[] for _ in range(200)]

for _ in range(int(input())):
    a,b = sys.stdin.readline().split()
    name[int(a)-1].append(b)

i = 0
while i != 200:
    if not name[i]:
        i += 1
    else:
        sys.stdout.write(f"{i+1} {name[i][0]}\n")
        name[i].pop(0)