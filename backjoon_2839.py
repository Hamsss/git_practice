N = int(input())

val = N//5
remain = N % 5

if val == 0 and remain%3 == 0:
    count = remain//3

elif val != 0: 
    if remain%3 != 0:
        a = 1
        for _ in range(0,val):
            if (remain + (a * 5)) % 3 == 0:
                count = (val - a) + ((remain + (a * 5)) // 3)
                break
            else:
                count = -1
                a += 1
    else:
        count = val + remain//3

else:
    count = -1
    
print(count)