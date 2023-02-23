N = int(input())

for i in range(2*N-1):
    if i < N:
        print(" " * (N - i - 1) + "*" * (1 + 2*i))
    else:
        print(" " * (i - N + 1) + "*" * (4*N - 2*i -3))