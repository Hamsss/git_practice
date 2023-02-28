word = []
find_max = 0
answer = []

for _ in range(5):
    a = list(map(str,input()))
    word.append(a)
    if find_max < len(a):
        find_max = len(a)

for i in range(find_max):
    for j in range(5):
        if i < len(word[j]):
            answer.append(word[j][i])
        else:
            pass
        
a = 0
while a != len(answer):
    print(answer[a], end = '')
    a += 1