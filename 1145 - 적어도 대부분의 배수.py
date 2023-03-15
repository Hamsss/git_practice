num_list = list(map(int, input().split()))
num = min(num_list)

while 1:
    count = 0
    for i in range(5):
        if num % num_list[i] == 0:
            count += 1
    if count >= 3:
        break
    num += 1

print(num)