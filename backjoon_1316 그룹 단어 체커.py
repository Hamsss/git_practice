N = int(input())
count = 0

for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            continue
        elif word[j] in word[j+1:]:
            count += 1
            break

print(N - count)
    