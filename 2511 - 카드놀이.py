A = list(map(int, input().split()))
B = list(map(int, input().split()))
vict = []
a_score = 0
b_score = 0
flag = 0

for i in range(10):
    if A[i] > B[i]:
        a_score += 3
        vict.append("A")
    elif A[i] < B[i]:
        b_score += 3
        vict.append("B")
    else:
        a_score += 1
        b_score += 1
        vict.append("D")
        
print(a_score, b_score)

if a_score > b_score:
    print("A")
elif a_score < b_score:
    print("B")
else:
    for i in range(1,11):
        if vict[-i] == "A":
            print("A")
            flag = 1
            break
        elif vict[-i] == "B":
            print("B")
            flag = 1
            break
    if flag == 0:
        print("D")