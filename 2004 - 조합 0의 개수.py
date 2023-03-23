n, m = map(int,input().split())

def count5(x):
    count5 = 0
    a = 5
    while x >= a:
        count5 += x // a
        a *= 5
    return count5

def count2(x):
    count2 = 0
    b = 2
    while x >= b:
        count2 += x // b
        b *= 2
    return count2

real_2 = count2(n) - count2(n-m) - count2(m)
real_5 = count5(n) - count5(n-m) - count5(m)

print(min(real_2,real_5))


