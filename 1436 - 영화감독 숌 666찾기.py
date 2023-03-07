N = int(input())
i = 666
count = 1
while N != 1:
    i += 1
    if '666' in str(i):
        count += 1
        if count == N:
            break
print(i)