a,b,n,w = map(int, input().split())
s = []
g = []

for sheep in range(1, n):
    goat = n - sheep
    if sheep * a + goat * b == w:
        s.append(sheep)
        g.append(goat)
        
if len(s) == 1:
    print(f"{s[0]} {g[0]}")
else:
    print(-1)
