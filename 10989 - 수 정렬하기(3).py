import sys

list = [0] * 10000
for _ in range(int(input())):
    list[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    while list[i] != 0:
        sys.stdout.write(f"{i+1}\n")
        list[i] -= 1
