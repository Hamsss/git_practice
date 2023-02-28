N = int(input())
num = N
i = 2

if N == 1:
    pass
else:
    while N / i != 1:
        if N % i == 0:
            print(i)
            N /= i
        else:
            i += 1
    print(i)
               