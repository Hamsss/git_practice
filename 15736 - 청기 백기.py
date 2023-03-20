def get_gcd(a,b):
    while a%b != 0:
        a, b = b, a%b
    return b

result = [0,3]+[0] * 1000

for i in range(2,1001):
    count = 0
    for j in range(1,i+1):
        if get_gcd(i,j) == 1:
            count += 2
    result[i] = count + result[i-1]

for _ in range(int(input())):
    print(result[int(input())])
    


    