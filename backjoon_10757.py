A, B = map(str, input().split())

flag = 0
result = ""

for i in range(1, max(len(A), len(B)) + 1):
    if i <= min(len(A), len(B)):
        temp = int(A[-i]) + int(B[-i]) + flag
    
    elif i > min(len(A), len(B)):
        if len(A) > len(B):
            temp = int(A[-i]) + flag
                
        elif len(A) < len(B):
            temp = int(B[-i]) + flag
    
    if temp >= 10:
        result += str(temp-10)
        flag = 1
    else:
        result += str(temp)
        flag = 0

if flag == 1:
    result += "1"
            
print(result[::-1])