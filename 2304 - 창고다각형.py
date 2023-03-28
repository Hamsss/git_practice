import sys
z_list = []
result = 0

for _ in range(int(input())): z_list.append(list(map(int,sys.stdin.readline().split())))
z_list.sort()

for i in range(len(z_list)):
    if z_list[i][1] > result:
        result = z_list[i][1]
        idx = i

high = z_list[0][1]

for i in range(idx):
    #정방향
    if z_list[i][1] > high:
        high = z_list[i][1] 
        result += z_list[i][1] * (z_list[i+1][0] - z_list[i][0])
    else: result += high*(z_list[i+1][0] - z_list[i][0])

high = z_list[-1][1]

for i in range(len(z_list)-1, idx, -1):
    #역방향
    if z_list[i-1][1] > high:
        result += high*(z_list[i][0] - z_list[i-1][0])
        high = z_list[i-1][1]
        
    else: result += high*(z_list[i][0] - z_list[i-1][0])

print(result)