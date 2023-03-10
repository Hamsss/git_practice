N = int(input())

count = 0

for Yonghun in range(1, N):
    for Namku in range(3, N):
        Takhee = N - Namku - Yonghun
        if Namku >= Yonghun + 2 and Takhee % 2 == 0 and Takhee > 0:
            count += 1

print(count)
            