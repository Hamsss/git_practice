import sys
n = int(input())
a = list(map(int,sys.stdin.readline().split()))
val = [0] * 51
answer = []

for i in a: val[i] += 1

for j in range(51):    
    if val[j] == j: answer.append(j)

if answer: print(max(answer))
else: print(-1)