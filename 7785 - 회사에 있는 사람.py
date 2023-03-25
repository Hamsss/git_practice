import sys
name_list = {}

for _ in range(int(input())):
    name, state = sys.stdin.readline().split()
    name_list[name] = state
    
a = []
keys = list(name_list.keys())
for i in keys:
    if name_list[i] == "enter": a.append(i)
    
a.sort(reverse = True)

for i in a: print(i)