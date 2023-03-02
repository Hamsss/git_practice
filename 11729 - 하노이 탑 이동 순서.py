import sys
def Hanoi(N, s, e):
    if N == 1:
        sys.stdout.write(f"{s} {e}\n") 
        return
    
    Hanoi(N - 1, s, 6-s-e)
    sys.stdout.write(f"{s} {e}\n")
    Hanoi(N - 1, 6-s-e, e)

N = int(sys.stdin.readline().strip())
sys.stdout.write(f"{2**N-1}\n")
Hanoi(N, 1, 3)

# 1914번
# if N > 20: sys.stdout.write(f"{2**N-1}\n")
# else:
#     sys.stdout.write(f"{2**N-1}\n")
#     Hanoi(N, 1, 3)