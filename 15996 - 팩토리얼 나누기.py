N, A = map(int,input().split())
cnt = 0
i = 2
num = A
while N >= num:
    cnt += N // num
    num = A**i
    i += 1
print(cnt)