T = int(input())
info = []

for i in range(T):
    H, W, N = map(int, input().split())
    a = N // H
    b = N % H
    num = 100

    if a == 0 and b != 0:
        num = num * N + 1   # 한 줄에서 끝날 때
    elif b == 0:
        num = num * H + a
    else:
        num = num * b + a + 1    # 보통 상황
    
    info.append(num)

for k in range(len(info)):
    print(info[k])