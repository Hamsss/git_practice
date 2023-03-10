def Fibo(n : int):
    return 0 if n == 0 else 1 if n == 1 else Fibo(n-1) + Fibo(n-2)

print(Fibo(int(input())))