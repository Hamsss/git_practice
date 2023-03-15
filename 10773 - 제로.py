import sys
num_list = [0]

for _ in range (int(input())):
    num = int(sys.stdin.readline())
    if num != 0:
        num_list.append(num)
    else:
        num_list.pop()

print(sum(num_list))