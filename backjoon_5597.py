std = []
non = []

for i in range(28):
    std.append(int(input()))
    
for i in range(1,31):
    flag = 0
    for j in range(28):
        if i == std[j]:
            flag = 1
            continue

    if flag == 0:
        non.append(i)

print(non[0])
print(non[1])
    
