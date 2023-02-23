word = []
find_max = 0
answer = []

for i in range(5):
    a = input()
    word.append(a)
    if find_max < len(a):
        find_max = len(a)


for i in range(find_max):
    for j in range(5):
        answer.append(word[j][i])