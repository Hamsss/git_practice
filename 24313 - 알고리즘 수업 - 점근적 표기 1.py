a_1, a_0 = map(int,input().split())
c = int(input())
n_0 = int(input())

f_n = a_1 * n_0 + a_0
c_gn = c * n_0

if f_n <= c_gn:
    print(1)
else:
    print(0)


