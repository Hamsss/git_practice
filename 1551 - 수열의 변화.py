N,K = map(int, input().split())
num_list = []
num_list.append(list(map(int, input().split(','))))

for i in range(K):
    change = []
    for j in range(len(num_list[i])-1):
        change.append(num_list[i][j+1] - num_list[i][j])
    num_list.append(change)

if K != 0: print(",".join(map(str, change)))
else : print(",".join(map(str, num_list[0])))