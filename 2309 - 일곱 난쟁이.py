dwarf = []

for _ in range(9):
    dwarf.append(int(input()))
    
height = sum(dwarf)

for i in range(0,8):
    for j in range(i+1,9):
        if height - dwarf[i] - dwarf[j] == 100:
            dwarf.pop(i)
            dwarf.pop(j-1)
            break
    if len(dwarf) == 7:
        break

dwarf.sort()

for i in range(7):
    print(dwarf[i])