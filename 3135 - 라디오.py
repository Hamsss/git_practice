start, end = map(int, input().split())
length = [abs(end - start)]

for _ in range(int(input())):
    length.append(abs(end - int(input())))

length_min = min(length)
print(length_min) if length[0] == length_min else print(length_min + 1)


    