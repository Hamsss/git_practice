import sys

count = 0
remain = 30

for _ in range(int(input())):
    time = int(sys.stdin.readline())
    if time <= remain:
        remain -= time
        if remain == 0:
            remain = 30
        count += 1
    elif time / 2 <= remain and time > remain:
        remain = 30
        count += 1
    else:
        remain = 30

print(count)