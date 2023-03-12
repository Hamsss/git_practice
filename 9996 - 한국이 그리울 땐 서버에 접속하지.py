import sys

N = int(input())
check = list(map(str, sys.stdin.readline().strip().split("*")))
answer = []

for _ in range(N):
    words = sys.stdin.readline().strip()
    
    if len(words) >= len(check[0]) + len(check[1]): 
        if words[0:len(check[0])] == check[0] and words[-len(check[1]):] == check[-1]:
            answer.append("DA")
        else:
            answer.append("NE")
    else:
        answer.append("NE")
        
for i in range(N):
    sys.stdout.write(f"{answer[i]}\n")