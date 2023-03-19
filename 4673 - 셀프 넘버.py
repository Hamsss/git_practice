import sys

num = set(range(1,10001))
temp = set()

for i in range(1,10001):
    for j in str(i): i += int(j)
    temp.add(i)

sort_num = sorted(num - temp)

for i in sort_num: sys.stdout.write(f"{i}\n")